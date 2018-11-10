import numpy as np
import datetime as dt
import random
import pandas_datareader.data as web

import gym
from gym import spaces
from gym.utils import seeding

class TraderEnv(gym.Env):

    def __init__(self, year = 2017, month = 1, day = 1, ticker = 'AAPL', capital = 500, volume = 10):
        self.action_space = spaces.Discrete(3)
        self.observation_space = spaces.Discrete(1)
        self.capital = capital
        self.balance = capital
        self.volume = volume
        self.iter = 0
        self.prev_state = 0
        self.data = self.get_data(year, month, day, ticker)

        self.prev_act = 0
    
    def get_data(self, year, month, day, ticker):
        start = dt.datetime(year, month, day)
        end = dt.datetime.now()
        df = web.DataReader(ticker, 'yahoo', start, end)
        price = df[['Low','High']].values

        return price, len(df)
  

    def step(self, action):
        # assert self.action_space.contains(action)
        low = np.round(self.data[0][self.iter][0], 2)
        high = np.round(self.data[0][self.iter][1], 2)

        state = random.uniform(low, high)
        reward = 0

        # Wait
        if action == 0:
            self.state = random.uniform(low, high)
        
        # Buy
        if action == 1: 

            if self.prev_act == 0:
                reward += 0

            if self.prev_act == 1:
                reward -= 1

            if self.prev_act ==  2 and self.prev_state < state:
                reward += 1
            else:
                reward -= 1

            self.balance -= state
            self.volume += 1 
            self.prev_state = state
            self.prev_act = 1
        
        # Sell
        if action == 2:

            if self.prev_act == 0:
                reward = +0

            if self.prev_act == 1 and self.prev_state < state:
                reward += 1

            if self.prev_act ==  2:
                reward -= 1
            else:
                reward += 1

            self.balance += state
            self.volume -= 1
            self.prev_state = state
            self.prev_act = 2

        done = False

        if  self.iter == self.data[1] - 1 or self.volume < 0 or self.balance < 0:
            done = True
        
        self.iter += 1

        # info = { 'reward': self.reward }
        
        return np.round(state, 2), reward, done


    def reset(self):
        self.state = 0
        self.reward = 0
        self.iter = 0
        self.balance = self.capital
        self.prev_state = 0
        self.volume = 10
        self.capital = 500

        return self.state

    def seed(self, seed=None):
        self.np_random, seed = seeding.np_random(seed)
        return [seed]