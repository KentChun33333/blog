import tensorflow as tf 
import numpy as np

class PolicyGradient:
    def __init__(self,n_actions, n_features, learning_rate=0.01,
                 reward_decay=0.95, output_graph=False):
        
        # External Information 
        self.n_actions = n_actions
        # =======================================================
        # [Thought-1]
        # =======================================================
        # Some State or Obseration with clear small set of action 
        # would be a problem with this method
        # we should have a better approach
        # =======================================================
        # [Thought-2]
        # All State should be better Normalized in some direction 
        # or some subset, or some layers , ... etc 
        # to -1 ~ 1 or 1 ~ 0 , for a better convergence
        # =======================================================
        # [Note]
        # =======================================================
        # Deep Q-Network is with an limitation that output or 
        # actions are discrete while the action like steering are
        # continuous in car racing.
        # =======================================================
        # [Note]
        # =======================================================
        # Google Deepmind has devised a new algorithm 
        # called Deep Deterministic Policy Gradients 
        # to tackle the continuous action space problem 
        # by combing 3 techniques together 
        # 1) Deterministic Policy-Gradient Algorithms
        # 2) Actor-Critic Methods
        # 3) Deep Q Network 
        # =======================================================

        # External Information 
        self.n_features = n_features
        
        # Internal Information 
        # learning Rate
        self.lr = learning_rate     
        
        # reward decay
        self.gamma = reward_decay   

        # The storage of Episode (List Type)
        self.ep_obs, self.ep_as, self.ep_rs = [], [], []    

        # build policy net
        self._build_net()   
        self.sess = tf.Session()

        if output_graph:    
            # tensorboard ::boolean::
            # $ tensorboard --logdir=logs
            # http://0.0.0.0:6006/
            # tf.train.SummaryWriter soon be deprecated, use following
            tf.summary.FileWriter("logs/", self.sess.graph)
        self.sess.run(tf.global_variables_initializer())

    def _build_net(self):
        with tf.name_scope('inputs'):
            self.tf_obs = tf.placeholder(tf.float32, 
                                         [None, self.n_features], name="observations")  
            # get_observation
            
            self.tf_acts = tf.placeholder(tf.int32, [None, ], name="actions_num")   
            # get_action we picked after get_observation 
            
            # get_long_term estimation value :: 
            # for every value corresponding to state-action 
            # by ::reward:: computation 
            self.tf_vt = tf.placeholder(tf.float32, [None, ], name="actions_value") 

        with tf.variable_scope('layer1'):
            # Hidden Layer
            W1 = tf.get_variable("W1", shape=[self.n_features, 10], 
                initializer=tf.random_normal_initializer(0., 0.2))
            b1 = tf.get_variable("b1", shape=[10, ], 
                initializer=tf.constant_initializer(0.01))
            layer1 = tf.matmul(self.tf_obs, W1) + b1

        with tf.variable_scope('layer2'):
            # Output Layer 
            W2 = tf.get_variable("W2", shape=[10, self.n_actions], 
                initializer=tf.random_normal_initializer(0., 0.2))
            b2 = tf.get_variable("b2", shape=[self.n_actions, ], 
                initializer=tf.constant_initializer(0.01))
            layer2 = tf.matmul(layer1, W2) + b2
            self.all_act_prob = tf.nn.softmax(layer2) 
            # the probability distribution of all actions

        with tf.name_scope('loss'):
            log_prob = tf.nn.sparse_softmax_cross_entropy_with_logits(self.all_act_prob, self.tf_acts) 
            # 所选 action 的概率 log 值
            loss = tf.reduce_mean(log_prob * self.tf_vt) 
            # (vt = 本reward + 衰减的未来reward) 引导参数的梯度下降

        with tf.name_scope('train'):
            self.train_op = tf.train.AdamOptimizer(self.lr).minimize(loss)
    
    def choose_action(self, observation):

        # ====================================================================
        # [Note]
        # ====================================================================
        # at the train_op, we feed tf_obs as with [[obs],[obs], ... , [obs]] 
        # with shape = (None, observation)
        # output :: prob_weights :: shape = (1,4)
        # ====================================================================

        prob_weights = self.sess.run(self.all_act_prob,
                                     feed_dict={self.tf_obs: observation[np.newaxis, :]}) 

        # According to the prob_weight to chose action 
        action = np.random.choice(range(prob_weights.shape[1]), 
                                  p=prob_weights.ravel()) 

        # ===============================================================
        # [Note] np.ravel() :: from (1,4) to (4,)
        # ===============================================================
        # Return a contiguous flattened array. 
        # A 1-D array, containing the elements of the input, 
        # is returned. A copy is made only if needed.
        # As of NumPy 1.10, the returned array will have the same type 
        # as the input array. (for example, a masked array will be 
        # returned for a masked array input) 
        # ===============================================================
        # [Note] np.random.choice( a, p= [] )
        # EX :: np.random.choice([0,1,2], p=np.array([0.1, 0.5, 0.4]))
        # where len(a) == len(p)
        # ===============================================================
        return action
    
    def store_transition(self, s, a, r):
        self.ep_obs.append(s)
        self.ep_as.append(a)
        self.ep_rs.append(r)
        
    def learn(self):
        # 衰减, 并标准化这回合的 reward
        discounted_ep_rs_norm = self._discount_and_norm_rewards()   

        # train on episode
        # SESS RUN :: train_op or [train_op, loss] + feed_dict = {key : np.array}
        self.sess.run(self.train_op, feed_dict={
             self.tf_obs: np.vstack(self.ep_obs),  
             # shape=[None, n_obs]
             self.tf_acts: np.array(self.ep_as), 
             # shape=[None, ]
             self.tf_vt: discounted_ep_rs_norm,
             # shape=[None, ]
        })
        self.ep_obs, self.ep_as, self.ep_rs = [], [], []    
        # 清空回合 data
        
        return discounted_ep_rs_norm    
        # 返回这一回合的 state-action value
    
    def _discount_and_norm_rewards(self):
        # discount episode rewards
        discounted_ep_rs = np.zeros_like(self.ep_rs)
        running_add = 0
        for t in reversed(range(0, len(self.ep_rs))):
            running_add = running_add * self.gamma + self.ep_rs[t]
            discounted_ep_rs[t] = running_add

        # normalize episode rewards
        discounted_ep_rs -= np.mean(discounted_ep_rs)
        discounted_ep_rs /= (np.std(discounted_ep_rs))
        return discounted_ep_rs

    def _discount_and_norm_rewards_2(self):
        # discount episode rewards
        discounted_ep_rs = np.zeros_like(self.ep_rs)
        running_add = 0
        for t in range(0, len(self.ep_rs)):
            running_add = running_add * self.gamma + self.ep_rs[t]
            discounted_ep_rs[t] = running_add

        # normalize episode rewards
        discounted_ep_rs -= np.mean(discounted_ep_rs)
        discounted_ep_rs /= np.std(discounted_ep_rs)
        return discounted_ep_rs

    def _discount_and_norm_rewards_3(self):
        # discount episode rewards
        discounted_ep_rs = np.zeros_like(self.ep_rs)
        running_add = 0
        for t in reversed(range(0, len(self.ep_rs))):
            running_add = running_add * self.gamma + self.ep_rs[t]
            discounted_ep_rs[t] = running_add

        return discounted_ep_rs

    def _discount_and_norm_rewards_4(self):
        # discount episode rewards
        discounted_ep_rs = np.zeros_like(self.ep_rs)
        running_add = 0
        for t in range(0, len(self.ep_rs)):
            running_add = running_add * self.gamma + self.ep_rs[t]
            discounted_ep_rs[t] = running_add
        return discounted_ep_rs



