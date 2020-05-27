import numpy as np 
import tensorflow as tf 


class IterativePolicyEvaluation():
"""
Evaluate a policy given an environment and 
a full description of the environment's dynamics.

Args:
    policy: [S, A] shaped matrix representing the policy.
    env: OpenAI env. 
    env.P represents the transition probabilities of the environment.
    env.P[s][a] is a (prob, next_state, reward, done) tuple.

Returns:
    Vector of length env.nS representing the value function.
"""
    def __init__(self, stateSet, actionSet, gamma, theta=1e-5):

        # State Space, Set  
        self.stateSet = stateSet

        # Action Space, Set 
        self.actionSet = actionSet

        # Reward discounting rate 
        self.gamma = gamma

        # if delta < theta, not iterating
        self.theta = theta

        # init delta
        self.delta = 0 

        # init V(S), use list to represent the fn 
        self.VS = np.zeros(len(stateSet))

        # use Matrix to represent the policy(a|s)
        self.policy = np.zeros((len(stateSet), len(actionSet)))

    def evaluate(self, policy, env, ):

        for s in range(env.nS):
            v = 0 

            # By use matrix-representation, 
            # we use enumerate to have action-encoded-number = a 
            # and policy[s] is the action_prob, 
            for a, action_prob in enumerate(policy[s]):
                # in open-ai gym
                # step function would return observations, reward, done and info
                # where prob and next_state is encoded in the observations
                
                for prob, next_state, reward, done in env.P[s][a]:
                    v += action_prob * prob * (reward + discount_factor * V[next_state])


        return pass



def policy_eval(policy, env, discount_factor=1.0, theta=0.00001):
"""
Evaluate a policy given an environment and 
a full description of the environment's dynamics.

Args:
    policy: [S, A] shaped matrix representing the policy.
    env: OpenAI env. 
    env.P represents the transition probabilities of the environment.
    env.P[s][a] is a (prob, next_state, reward, done) tuple.

Returns:
    Vector of length env.nS representing the value function.
"""
    # Start with a random (all 0) value function 
    V = np.zeros(env.nS)
    while True:
        delta = 0
        # For each state, perform a "full backup"
        for s in range(env.nS):
            v = 0
            # Look at the possible next actions
            for a, action_prob in enumerate(policy[s]):

                # For each action, look at the possible next states...
                for  prob, next_state, reward, done in env.P[s][a]:
                    # Calculate the expected value
                    v += action_prob * prob * (reward + discount_factor * V[next_state])
            # How much our value function changed (across any states)
            delta = max(delta, np.abs(v - V[s]))
            V[s] = v
        # Stop evaluating once our value function change is below a threshold
        if delta < theta:
            break
    return np.array(V)





