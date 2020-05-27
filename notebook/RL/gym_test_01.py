import gym
env = gym.make('MountainCar-v0')
env.reset()
for i in range(1000):
    env.render()
    ob, reward, done, _ = env.step(env.action_space.sample()) # take a random action
    if done is True:
        print i
        env.reset()

    # observation is numpy object 
    print 


import numpy as np 
import pandas as pd 

