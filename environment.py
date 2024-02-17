from typing import Tuple, List
from parameters import Parameters
import numpy as np
from ale_py import ALEInterface
from ale_py.roms import Frostbite, UpNDown
from atari import Atari
import gymnasium as gym
import random

class Environment:
    """
    This class serves as an interface to ensure that any Environment subtype
    implements a reset method and a step method. This is used to abstract away
    the differences between envrionments and provide a common wrapper to use with the model.
    """
    def reset(self) -> np.array:
        """
        Reset the environment back to its initial state.

        :return: the initial state/observation.
        """
        raise NotImplementedError("Don't use Environment class directly..")

    def step(self, action) -> Tuple[np.array, float, bool]:
        """
        Do the provided action in the environment

        :param action: the action to take
        :return: the state/observation after the action, the reward associated with the action, whether or not the agent has reached a terminal state
        """
        raise NotImplementedError("Don't use Environment class directly.")

class GymEnvironment(Environment):
    """
    This class implements the Environment interface for the OpenAI Gymnasium.
    """
    def __init__(self):
        self.env = gym.make(Parameters.ENVIRONMENT)
        
    def reset(self) -> np.array:
        """
        Reset the environment back to its initial state.

        :return: the initial state/observation.
        """
        return np.array(self.env.reset()[0]).flatten()

    def step(self, action: str) -> Tuple[np.array, float, bool]:
        """
        Do the provided action in the environment

        :param action: the action to take
        :return: the state/observation after the action, the reward associated with the action, whether or not the agent has reached a terminal state
        """
        index: int = Parameters.ACTIONS.index(action)
        state, reward, isTerminated, isTruncated, _ = self.env.step(index)
        return (np.array(state).flatten(), reward, isTerminated or isTruncated)

class ALEEnvironment(Environment):
    """
    This class implements the Environment interface for the Atari Learning Environment (ALE).
    """
    def __init__(self):
        self.ale = ALEInterface()
        
        if Parameters.ENVIRONMENT == "Frostbite":
            return self.ale.loadROM(Frostbite)
        elif Parameters.ENVIRONMENT == "UpNDown":
            return self.ale.loadROM(UpNDown)
        else:
            raise RuntimeError("Environment could not be loaded: ROM not found.")

    def reset(self) -> np.array:
        """
        Reset the environment back to its initial state.

        :return: the initial state/observation.
        """
        self.ale.reset_game()
        return Atari.preprocess(self.ale.getScreenRGB())

    def step(self, action: int) -> Tuple[np.array, float, bool]:
        """
        Do the provided action in the environment

        :param action: the action to take
        :return: the state/observation after the action, the reward associated with the action, whether or not the agent has reached a terminal state
        """
        reward = self.ale.act(action)
        return (Atari.preprocess(self.ale.getScreenRGB()), reward, self.ale.game_over())

    
