import numpy as np
import matplotlib.pyplot as plt

import gym
from gym import spaces
from gym.utils import seeding

# np.random.seed(0)

class TraderEnv(gym.Env):

    def __init__(self, interval_size = 365):
    	self.action_space = spaces.Discrete(3)
    	self.observation_space = spaces.Discrete(interval_size)
    	self.reward = np.zeros(interval_size)
    	self.state = np.random.randint(50, size=interval_size)
    	self.state_count = 0
    	
    def seed(self, seed=None):
        self.np_random, seed = seeding.np_random(seed)
        return [seed]

    def step(self, action):
    	assert self.action_space.contains(action)

        if action == 0: # Wait
            self.reward[state_count] = self.reward[state_count - 1]
            self.state[state_count] = np.random.randint(50)
        
        if action == 1: # Buy
        	self.reward[state_count] = self.reward[state_count - 1] - self.state
        	self.acted_state = self.state
            self.state[state_count] = np.random.randint(50)
        
        if action == 2: # Sell
        	self.reward[state_count] = self.reward[state_count - 1] + self.state
        	self.acted_state = self.state 
            self.state[state_count] = np.random.randint(50)

        self.state_count += 1

        done = False
        if self.state_count >= interval_size: 
            done = True
       	
       
        return self.state, reward, done, {}

    def _plot(self):
    	interval = np.arange(1, interval_size, 1)
		reward = self.reward
		price = self.state

		plt.subplot(2, 1, 1)
		plt.plot(interval, reward)
		plt.title('Stock Prices and Reward Visualization')
		plt.ylabel('Reward')

		plt.subplot(2, 1, 2)
		plt.plot(interval, price)
		plt.xlabel('Interval')
		plt.ylabel('Price')

		plt.show()

    def reset(self):
        self.state = np.random.randint(50)
        return self.state