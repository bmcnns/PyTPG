from typing import Tuple, List
from parameters import Parameters
import gym

class Environment:

    def __init__(self):
        self.env = gym.make("LunarLander-v2")
        
    def reset(self) -> List[float]:
        return self.env.reset()[0]

    def step(self, action: str) -> Tuple[List[float], float, bool]:
        index: int = Parameters.ACTIONS.index(action)
        assert(type(index) == int)
        
        try:
            state, reward, isTerminated, isTruncated, _ = self.env.step(index)
            return (state, reward, isTerminated or isTruncated) 
        except:
            print(f"ERROR: index is {index}")
