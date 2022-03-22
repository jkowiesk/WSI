import numpy as np
from random import random, choice


class Agent():
    def __init__(self, env, discount=0.98, alpha=0.5, action_prob=1):
        self.action_size = env.action_space.n
        self.state_size = env.observation_space.n
        self.q = np.random.random([self.state_size, self.action_size])

        self.discount = discount
        self.alpha = alpha
        self.action_prob = action_prob

    def get_action_learn(self, state):
        if random() < self.action_prob:
            return choice(range(self.action_size))
        else:
            return np.argmax(self.q[state])

    def get_action(self, state):
        return np.argmax(self.q[state])

    def learn(self, state, action, next_state, reward, done):
        if done:
            target = reward
            self.action_prob *= 0.99
        else:
            target = reward + self.discount * max(self.q[next_state])

        q_gradient = target - self.q[state][action]
        self.q[state][action] += self.alpha * q_gradient
