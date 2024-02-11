from typing import List
import random
from program import Program
import numpy as np
from uuid import uuid4
from typing import List
from copy import deepcopy
from parameters import Parameters

import numpy as np

class Team:
    def __init__(self, programPopulation: List[Program]):
        """
        Generates a team with a number of randomly assigned programs.
        A team has at least two programs but may have up to MAX_INITIAL_TEAM_SIZE programs.
        It is guaranteed that a team has at least two atomic actions.
        :param programPopulation: All programs (at the time of the team's creation)
        :return: A new team
        """
        self.id: UUID = uuid4()

        # A team is a champion if it is the best performing team in a generation
        self.scores: List[float] = []
        
        # Choose two programs from the program population
        self.programs: List[Program] = [] 
        actions: List[str] = []

        self.luckyBreaks: int = 0

        size: int = random.randint(2, Parameters.MAX_INITIAL_TEAM_SIZE)

        while len(list(set(actions))) < 2:
            self.programs: List[Program] = random.sample(programPopulation, k=size)
            actions: List[str] = [ program.action for program in self.programs] 

    # Choose the program with the highest confidence
    def getAction(self, teamPopulation: List['Team'], state: np.array, visited: List[str] = []) -> str:
        """
        Returns the team's suggested action by choosing the action of the highest-bidding program.
        If the highest-bidding program is a reference to another team, recurse until the action is atomic.
        If the policy graph has a cycle, any team is only visited once.

        :param teamPopulation: All teams
        :param state: The feature vector representing the state/observation
        :param visited: Used internally in recursive calls, ensures this method does not recurse forever when a cycle is encountered.

        :return: an atomic action
        """
        visited.append(self)

        sortedPrograms = sorted(self.programs, key=lambda program: program.bid(state)['confidence'])
            
        for program in sortedPrograms:
            if program.action in Parameters.ACTIONS:
                if program.action == None:
                    raise RuntimeError("A NONE ACTION WAS ENCOUNTERED HERE")
                return program.action
            else:
                for team in teamPopulation:
                    if str(team.id) == program.action:
                        return team.getAction(teamPopulation, state, visited)
                return random.choice(Parameters.ACTIONS)
                raise RuntimeError(f"Team {self.id} points to team {program.action}, and that team does not exist within the population.")

    def getFitness(self):
        """
        This method is used to define the fitness of a team.
        By default, fitness is the score from the previous generation.

        :return: The fitness score
        """
        return self.scores[-1]

    # Given a parent team, a new offspring team is cloned and mutated
    def copy(self) -> "Team":
        """
        Clones an existing team
        
        If the original team has 'lucky breaks', they are not carried over to the cloned team.
        The clone is given a new ID such that no two teams have the same ID.
        
        :return: A new team with identical behaviour to the team that was cloned.
        """
        clone: 'Team' = deepcopy(self)
        clone.referenceCount = 0
        clone.luckyBreaks = 0
        clone.id = uuid4()
        return clone
