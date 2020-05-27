from tkinter_maze_2 import GridWord 

from NC_policy_gradient_baseline import PolicyGradientBaseline

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
    logger = DebugLog('Policy Gradient Baseline')

# init Network
RL = PolicyGradientBaseline(
    n_actions     = len(env.action_space),
    n_features    = len(env.position)    ,
    learning_rate = 0.001               ,
    reward_decay=0.99, 
)

for i_episode in range(35100):
    observation = env.reset()
    step=0
    while True:
        action = RL.choose_action(observation)

        if arg.visualize==1:
            env.render()

        observation_, reward, done , _ = env.step(action)
        RL.store_transition(observation, action, reward) 

        if i_episode > 200 and step > 3 and step%5==0:
        	# TD learn
        	vt = RL.learn() 

        if done :
            ep_rs_sum = sum(RL.ep_rs)

            if 'running_reward' not in globals():
                running_reward = ep_rs_sum
            else:
                running_reward = running_reward * 0.9 + ep_rs_sum * 0.1
            if arg.logger == 1: 
                logger.warn("episode : {}. reward : {}".format(i_episode, running_reward))

            
            # learn and out put vt, this value is useful
            # EP-learn
            # vt = RL.learn() 
            if i_episode > 45000:
                plt.plot(vt)    # plot 这个回合的 vt
                plt.xlabel('episode steps')
                plt.ylabel('normalized state-action value')
                plt.show()
            break

        observation = observation_
