# Robinzon Envirinment for OpenAI Gym
# Vasyl Tsykhmystro, November 2020

import gym
from gym import error, spaces, utils
from gym.utils import seeding

import logging
logger = logging.getLogger(__name__)

class RobinzonEnv(gym.Env):
    metadata = {'render.modes': ['human']}

    def __init__(self):
        self.boat = 100
        self.status = True

        self.viewer = None

        self.action_space = spaces.Discrete(18)
        self.observation_space = []

        self.seed()
        self.reset()


    def step(self, action):
        # lassert self.action_space.contains(action), f'{action} ({type(action)}) invalid'
        # make a boat
        if action == 0:
            self.boat -= 1
        reward = self._get_reward()
        ob = [self.boat]
        done = self.boat == 0
        return ob, reward, done, {}

    def reset(self):
        self.boat = 100
        return self.boat

    def render(self, mode='human'):
        pass

    def close(self):
        pass

    def _get_reward(self):
        """ Reward is given for scoring a goal. """
        if (self.boat == 0):
            return 100
        else:
            return -1

ACTION_MEANING = {
    0 : 'Built a boat',
    1 : 'Stocked up with water from the stream',
    2 : 'Dug a well',
    3 : 'Cleaned the well',
    4 : 'Collected fruit',
    5 : 'Made gear',
    6 : 'Was fishing',
    7 : 'Repaired gear',
    8 : 'Built a farm',
    9 : 'Worked on the farm',
    10 : 'Manufactured weapons',
    11 : 'Hunted',
    12 : 'Renovated dwelling',
    13 : 'Dug a dugout',
    14 : 'Built a house',
    15 : 'Repaired clothes',
    16 : 'Sewed a set of clothes',
    17 : 'Sewing clothes from skins',
}