from typing import Tuple, List
from parameters import Parameters
import gym
import numpy as np

"""
This Environment class serves as a generic interface to ANY environment
and forces the implementation of functions: reset and step.
"""
class Environment:

    """ Creates an environment based on Parameters.ENVIRONMENT.
        A parameter is passed to ensure the action space is discrete.
    """
    def __init__(self):
        self.env = gym.make(Parameters.ENVIRONMENT, continuous=False)
        
    """
    Reset the environment to its initial state.
    Returns observations
    """
    def reset(self) -> List[float]:
        return np.array(self.env.reset()[0]).flatten()

    def step(self, action: str) -> Tuple[List[float], float, bool]:
        index: int = Parameters.ACTIONS.index(action)
        assert(type(index) == int)
        
        try:
            state, reward, isTerminated, isTruncated, _ = self.env.step(index)
            return (np.array(state).flatten(), reward, isTerminated or isTruncated) 
        except:
            print(f"ERROR: index is {index}")
