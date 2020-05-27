
import tensorflow as tf 
import numpy as np
class PolicyGradientBaseline:
    def __init__(self,n_actions, n_features, learning_rate=0.01,
                 reward_decay=0.95, output_graph=False):
        self.n_actions = n_actions
        self.n_features = n_features
        self.lr = learning_rate   

        # according to tf_vt which
        self.state_lr  = 0.01

        self.gamma = reward_decay   
        self.ep_obs, self.ep_as, self.ep_rs = [], [], []    
        self._build_net()   
        self._state_estimator()
        self._update_ops()
        self.sess = tf.Session()
        if output_graph:    
            tf.summary.FileWriter("logs/", self.sess.graph)
        self.sess.run(tf.global_variables_initializer())

    def _build_net(self):
        with tf.name_scope('inputs'):
            self.tf_obs = tf.placeholder(tf.float32, 
                                         [None, self.n_features], name="observations")  
            self.tf_acts = tf.placeholder(tf.int32, [None, ], name="actions_num")   
            self.tf_vt = tf.placeholder(tf.float32, [None, ], name="actions_value") 
        with tf.variable_scope('layer1'):
            W1 = tf.get_variable("W1", shape=[self.n_features, 10], 
                initializer=tf.random_normal_initializer(0., 0.2))
            b1 = tf.get_variable("b1", shape=[10, ], 
                initializer=tf.constant_initializer(0.01))
            layer1 = tf.matmul(self.tf_obs, W1) + b1
        with tf.variable_scope('layer2'):
            W2 = tf.get_variable("W2", shape=[10, self.n_actions], 
                initializer=tf.random_normal_initializer(0., 0.2))
            b2 = tf.get_variable("b2", shape=[self.n_actions, ], 
                initializer=tf.constant_initializer(0.01))
            layer2 = tf.matmul(layer1, W2) + b2
            self.all_act_prob = tf.nn.softmax(layer2) 

    def _state_estimator(self):
        with tf.name_scope('state_estimator_layer_1'):
            W1 = tf.get_variable("W1", shape=[self.n_features, 10],
                initializer= tf.zeros_initializer())
            b1 = tf.get_variable("b1", shape=[5, ], 
                initializer=tf.constant_initializer(0.01))
            layer1 = tf.matmul(self.tf_obs, W1) + b1

        with tf.name_scope('state_estimator_layer_2'):
            W2 = tf.get_variable("W2", shape=[5, 1],
                initializer= tf.zeros_initializer())
            b2 = tf.get_variable("b2", shape=[1, ], 
                initializer=tf.constant_initializer(0.01))  
            layer2 = tf.matmul(layer1, W2) + b2
            out = tf.nn.softmax(layer2) 
            self.state_value = out

    def _update_ops(self):
        with tf.name_scope('state_estimator_loss'):
            self.state_estimator_loss = tf.nn.softmax(tf.reduce_mean(
                                        self.tf_vt)) - self.state_value

        with tf.name_scope('state_estimator_train'):
            self.state_train_op = tf.train.AdamOptimizer(
                                self.state_lr).minimize(self.state_estimator_loss)

        with tf.name_scope('loss'):
            log_prob = tf.nn.sparse_softmax_cross_entropy_with_logits(
                                      self.all_act_prob, self.tf_acts) 
            
            loss = tf.reduce_mean(log_prob * self.tf_vt) + self.state_estimator_loss

        with tf.name_scope('train'):
            self.train_op = tf.train.AdamOptimizer(self.lr).minimize(loss)

    def choose_action(self, observation):
        prob_weights = self.sess.run(self.all_act_prob,
                                     feed_dict={self.tf_obs: observation[np.newaxis, :]}) 
        action = np.random.choice(range(prob_weights.shape[1]), 
                                  p=prob_weights.ravel()) 
        return action
    def store_transition(self, s, a, r):
        self.ep_obs.append(s)
        self.ep_as.append(a)
        self.ep_rs.append(r)

    def learn(self):
        discounted_ep_rs_norm = self._discount_and_norm_rewards()   
        self.sess.run([self.train_op, self.state_train_op], feed_dict={
             self.tf_obs: np.vstack(self.ep_obs),  
             self.tf_acts: np.array(self.ep_as), 
             self.tf_vt: discounted_ep_rs_norm,
        })
        self.ep_obs, self.ep_as, self.ep_rs = [], [], []    
        return discounted_ep_rs_norm    

    def _discount_and_norm_rewards(self):
        discounted_ep_rs = np.zeros_like(self.ep_rs)
        running_add = 0
        for t in reversed(range(0, len(self.ep_rs))):
            running_add = running_add * self.gamma + self.ep_rs[t]
            discounted_ep_rs[t] = running_add
        discounted_ep_rs -= np.mean(discounted_ep_rs)
        discounted_ep_rs /= (np.std(discounted_ep_rs))
        return discounted_ep_rs

    def _discount_and_norm_rewards_2(self):
        discounted_ep_rs = np.zeros_like(self.ep_rs)
        running_add = 0
        for t in range(0, len(self.ep_rs)):
            running_add = running_add * self.gamma + self.ep_rs[t]
            discounted_ep_rs[t] = running_add
        discounted_ep_rs -= np.mean(discounted_ep_rs)
        discounted_ep_rs /= np.std(discounted_ep_rs)
        return discounted_ep_rs

    def _discount_and_norm_rewards_3(self):
        discounted_ep_rs = np.zeros_like(self.ep_rs)
        running_add = 0
        for t in reversed(range(0, len(self.ep_rs))):
            running_add = running_add * self.gamma + self.ep_rs[t]
            discounted_ep_rs[t] = running_add
        return discounted_ep_rs

    def _discount_and_norm_rewards_4(self):
        discounted_ep_rs = np.zeros_like(self.ep_rs)
        running_add = 0
        for t in range(0, len(self.ep_rs)):
            running_add = running_add * self.gamma + self.ep_rs[t]
            discounted_ep_rs[t] = running_add
        return discounted_ep_rs
