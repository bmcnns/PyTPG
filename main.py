from model import Model

import random
from typing import List
from environment import Environment
from debugger import Debugger
import sys

def main():

    sys.setrecursionlimit(1500)
    environment: Environment = Environment()
    model: Model = Model()
    debugger: Debugger = Debugger()

    try:
        model.fit(environment, 100, 1000)
    except RuntimeError as e:
        print(debugger.getInformation(model.programPopulation, model.teamPopulation))
        raise e
    
if __name__ == "__main__":
    main()
