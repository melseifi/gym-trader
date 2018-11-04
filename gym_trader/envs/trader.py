import numpy as np

import gym
from gym import spaces
from gym.utils import seeding

# np.random.seed(0)

class TraderEnv(gym.Env):

    def __init__(self):
        self.interval_size = 365
        self.action_space = spaces.Discrete(3)
        self.observation_space = spaces.Discrete(1)
        self.reward = 0
        self.state = 0
        self.state_count = 0
        
    def seed(self, seed=None):
        self.np_random, seed = seeding.np_random(seed)
        return [seed]

    def step(self, action):
        assert self.action_space.contains(action)

        # Wait
        if action == 0:
            self.state = np.random.randint(50)
        
        # Buy
        if action == 1:
            self.reward= self.reward - self.state
            self.state = np.random.randint(50)
        
        # Sell
        if action == 2:
            self.reward = self.reward + self.state
            self.state = np.random.randint(50)

        self.state_count += 1

        done = False
        if self.state_count >= self.interval_size: 
            done = True
        
        info = { 'reward': self.reward, 'interval':self.interval_size }
        
        return self.state, self.reward, done, info


    def reset(self):
        self.state = 0
        return self.state