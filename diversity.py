from team import Team
from typing import Dict, List
from collections import deque
import numpy as np
import math
from parameters import Parameters
import random

class Diversity:

	cache: deque[List[np.array]] = deque(maxlen=50)
	profiles: deque[str] = deque(maxlen=Parameters.POPULATION_SIZE)

	@staticmethod
	def updateCache(state: np.array):
		Diversity.cache.append(state)

	@staticmethod
	def getProfile(teamPopulation: List[Team], team: Team) -> List[str]:
		profile = [ team.getAction(teamPopulation, state) for state in Diversity.cache ] 
		return profile
