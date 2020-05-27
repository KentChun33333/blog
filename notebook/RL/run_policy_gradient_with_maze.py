from policy_gradient import PolicyGradient
from tkinter_maze_2 import GridWord
import tensorflow as tf 
import matplotlib.pyplot as plt
import time
import common_cli
from common_log import DebugLog

# init GridWord where size is from common_cli
arg = common_cli.main()
env = GridWord(arg.mazeSize,arg.mazeSize) 

# init Log 
if arg.logger == 1: 
    logger = DebugLog('Policy Gradient')

# init Network
RL = PolicyGradient(
    n_actions     = len(env.action_space),
    n_features    = len(env.position)    ,
    learning_rate = 0.001               ,
    # =============================================================
    # [Note]
    # =============================================================
    # if learning rate large => the action tend to be discrete
    # if learning rate small => train longer but tend to have 
    # more continous actions or more diversity of actions 
    # in this case, if we use 0.1, we will get to the local-minimum 
    # like go a streight line 
    # ============================================================= 

    # gamma 
    # 0.85 :: converge :: has relation with reward setting :: have change to converge
    # 0.5  :: not
    # 0.1  :: not

    reward_decay=0.99, 

    # output_graph=True,    # 输出 tensorboard 文件
)

for i_episode in range(35100):
    observation = env.reset()
    while True:
        action = RL.choose_action(observation)

        # according to the input to see whether visualize or not
        if arg.visualize==1:
            env.render()
        # state,reward, done
        observation_, reward, done , _ = env.step(action)
        RL.store_transition(observation, action, reward)    
        # Storage the trainsition in this episode
        # Update the Gridword vis

        # ==========================================================
        # [Note]
        # ==========================================================
        # this is not TD-learning 
        # this is like Monte-Carlo, a full-backup, learn by EPISODE
        # this Cause some problems.
        # ==========================================================

        if done :
            # since policy network in grid_world have the change to stock
            # we use _step to constrain a maz_step for a Episode
            ep_rs_sum = sum(RL.ep_rs)

            if 'running_reward' not in globals():
                running_reward = ep_rs_sum
            else:
                running_reward = running_reward * 0.9 + ep_rs_sum * 0.1
            if arg.logger == 1: 
                logger.warn("episode : {}. reward : {}".format(i_episode, running_reward))

            
            # learn and out put vt, this value is useful
            vt = RL.learn() 
            if i_episode > 45000:
                plt.plot(vt)    # plot 这个回合的 vt
                plt.xlabel('episode steps')
                plt.ylabel('normalized state-action value')
                plt.show()
            break

        observation = observation_

# ======================================================================
# [Note]
# ======================================================================
# Monte-Carlo Policy-Gradient may be not suitable for multi-ternal task
# It would reinforce the EPSODE-loop
# 