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
        self.res_water = 0
        self.res_food = 1

        self.alive = True

        self.viewer = None

        self.action_space = spaces.Discrete(18)
        self.observation_space = []

        self.seed()
        self.reset()

    def check_for_alive(self):
        self.alive = (self.res_water >= 0) #and (self.res_food >= 0)

    def day_passed(self):
        self.res_water -= 1
        self.res_food -= 1
        # still alive?
        self.check_for_alive()

    def do_day_task(self, action):
        # Built a boat
        if action == 0:
            self.boat -= 1
        # Stocked up with water from the stream
        if action == 1:
            self.res_water += 5
        # Collected fruit
        if action == 4:
            self.res_food += 3

    def step(self, action):
        # lassert self.action_space.contains(action), f'{action} ({type(action)}) invalid'
        # do day task
        self.do_day_task(action)
        # day passed
        self.day_passed()
        # reward
        reward = self._get_reward()
        ob = [self.boat, self.alive, self.res_water, self.res_food]
        # Win or Lose
        done = (self.boat == 0) and (self.alive)
        return ob, reward, done, {}

    def reset(self):
        self.boat = 100
        self.res_water = 0
        self.res_food = 1
        return self.boat

    def render(self, mode='human'):
        pass

    def close(self):
        pass

    def _get_reward(self):
        """ Reward is given for scoring a goal. """
        if self.alive:
            if (self.boat == 0):
                return 100
            elif (self.res_water >= 0): #and (self.res_food >= 0):
                return 1
            else:
                return -1
        else:
            return -1000

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