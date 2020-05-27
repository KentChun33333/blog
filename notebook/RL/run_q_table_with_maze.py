"""
Sarsa is a online updating method for Reinforcement learning.

Unlike Q learning which is a offline updating method, Sarsa is updating while in the current trajectory.

You will see the sarsa is more coward when punishment is close because it cares about all behaviours,
while q learning is more brave because it only cares about maximum behaviour.
"""

from tkinter_maze_2 import GridWord as Maze
from q_table_learning import QLearningTable
import common_cli


def run_maze(RL, episode_number=1000):
    '''description:
    run_maze = learn the policy 

    input:
      - RL : Algorithm Class
      - episode_number : int, iteration-times

    '''
    
    for episode in range(episode_number):
        # initial observation
        observation = env.reset()
        step = 0
        while True:
            # fresh env
            env.render()

            # RL choose action based on observation
            action = RL.choose_action(observation)

            # RL take action and get next observation and reward
            observation_, reward, done, _ = env.step(action)

            # RL learn
            RL.learn(str(observation), action, reward, str(observation_))

            # swap observation
            observation = observation_

            # break while loop when end of this episode
            if done:
                break
            step += 1

    # end of game
    print('game over')
    env.destroy()


if __name__ == "__main__":
    # maze game
    arg = common_cli.main()
    env = Maze(arg.mazeSize,arg.mazeSize)
    RL = QLearningTable(actions=env.action_space,
                      learning_rate=0.01,
                      reward_decay=0.9,
                      e_greedy=0.9,
                      )
    run_maze(RL,2000)
    