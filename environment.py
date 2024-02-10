from typing import Tuple, List
from parameters import Parameters
import numpy as np
from ale_py import ALEInterface
from ale_py.roms import Frostbite, UpNDown
from atari import Atari
import random

class Environment:

    def reset(self) -> np.array:
        raise NotImplementedError("Don't use Environment class directly..")

    def step(self, action) -> Tuple[np.array, float, bool]:
        raise NotImplementedError("Don't use Environment class directly.")

class GymEnvironment(Environment):

    def __init__(self):
        self.env = gym.make(Parameters.ENVIRONMENT)
        
    def reset(self) -> np.array:
        return np.array(self.env.reset()[0]).flatten()

    def step(self, action: str) -> Tuple[np.array, float, bool]:
        index: int = Parameters.ACTIONS.index(action)
        state, reward, isTerminated, isTruncated, _ = self.env.step(index)
        return (np.array(state).flatten(), reward, isTerminated or isTruncated)

class ALEEnvironment(Environment):

    def __init__(self, environment: str):
        self.ale = ALEInterface()
        
        if environment == "Frostbite":
            return self.ale.loadROM(Frostbite)
        elif environment == "UpNDown":
            return self.ale.loadROM(UpNDown)
        else:
            raise RuntimeError("Environment could not be loaded: ROM not found.")
    
    def reset(self) -> np.array:
        self.ale.reset_game()
        return Atari.preprocess(self.ale.getScreenRGB())

    def step(self, action: int) -> Tuple[np.array, float, bool]:
        reward = self.ale.act(action)
        return (Atari.preprocess(self.ale.getScreenRGB()), reward, self.ale.game_over())

    
