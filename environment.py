from typing import Tuple, List
from parameters import Parameters
import gym
import numpy as np

class Environment:

    def __init__(self):
        self.env = gym.make(Parameters.ENVIRONMENT, continuous=False)
        
    def reset(self) -> List[float]:
        return np.array(self.env.reset()[0]).flatten()

    def step(self, action: str) -> Tuple[List[float], float, bool]:
                    print(state)
        index: int = Parameters.ACTIONS.index(action)
        assert(type(index) == int)
        
        try:
            state, reward, isTerminated, isTruncated, _ = self.env.step(index)
            return (np.array(state).flatten(), reward, isTerminated or isTruncated) 
        except:
            print(f"ERROR: index is {index}")
