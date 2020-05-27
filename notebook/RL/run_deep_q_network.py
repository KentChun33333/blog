"""
Sarsa is a online updating method for Reinforcement learning.
Unlike Q learning which is a offline updating method, Sarsa is updating while in the current trajectory.

You will see the sarsa is more coward when punishment is close because it cares about all behaviours,
while q learning is more brave because it only cares about maximum behaviour.
"""

from tkinter_maze_2 import GridWord as Maze
from deep_q_network import DeepQNetwork
import common_cli

arg = common_cli.main()

def run_maze():
    step = 0
    for episode in range(16000):
        # initial observation
        observation = env.reset()
        while True:        
            # fresh env
            env.render()
            # RL choose action based on observation
            action = RL.choose_action(observation)

            # RL take action and get next observation and reward
            observation_, reward, done, _ = env.step(action)

            RL.store_transition(observation, action, reward, observation_)
            if step > 2000 and env.ratio > 0.4:
              # fixed action and not going to learn
              env.epsilon = 1.
              pass 
            elif step>200 and step % 5 ==0:
              RL.learn()

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
    env = Maze(arg.mazeSize, arg.mazeSize)
    RL = DeepQNetwork(n_actions=len(env.action_space),
    n_features=len(env.position),
    #env.n_actions, env.n_features,
                      learning_rate=0.01,
                      reward_decay=0.9,
                      e_greedy=0.9,
                      hidden_layers=[10, 10],
                      replace_target_iter=200,
                      memory_size=2000,
                      # output_graph=True
                      )
    env.after(100, run_maze)
    env.mainloop()
    RL.plot_cost()