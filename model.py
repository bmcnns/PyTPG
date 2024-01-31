from environment import Environment
from program import Program
from team import Team
from mutator import Mutator
from parameters import Parameters

import random
from typing import List, Tuple, Dict

class Model:

    # A model consists of a population of teams and a population of programs.
    """ A model consists of a population of teams and a population of programs."""
    def __init__(self):

        # Initialize the program population
        self.programPopulation: List[Program] = [ Program() for _ in range(Parameters.INITIAL_PROGRAM_POPULATION)]

        # Initialize the team population
        self.teamPopulation: List[Team] = [ Team(self.programPopulation) for _ in range(Parameters.POPULATION_SIZE)]

        for team in self.teamPopulation:
            team.referenceCount = 0

        self.data: Dict[str, float] = {}
        for team in self.teamPopulation:
            self.data[team.id] = 0.0 

    def getRootTeams(self) -> List[Team]:
        rootTeams: List[Team] = []
        for team in self.teamPopulation:
            if team.referenceCount == 0:
                rootTeams.append(team)

        return rootTeams

    def fit(self, environment: Environment, numGenerations: int, maxStepsPerGeneration: int) -> None:

        for generation in range(1, numGenerations+1):
            for teamNum, team in enumerate(self.getRootTeams()):

                state = environment.reset()
                score = 0
                step = 0
                print(f"Generation #{generation} Team #{teamNum + 1} ({team.id})")

                while True:


                    action = team.getAction(self.teamPopulation, state)
                    
                    state, reward, finished = environment.step(action)

                    score += reward
                    step += 1

                    if finished or step == maxStepsPerGeneration:
                        break

                self.data[team.id] = score
                # assign score to team
                print(f"Team finished with score: {score}")

            print("\nGeneration complete.\n")
            
            self.select(self.data, generation)
            self.data = {}

            self.evolve()

    def cleanProgramPopulation(self) -> None:
        inUseProgramIds: List[str] = []
        for team in self.teamPopulation:
            for program in team.programs:
                inUseProgramIds.append(program.id)

        for program in self.programPopulation:
            if program.id not in inUseProgramIds:
                self.programPopulation.remove(program)

    # Remove uncompetitive teams from the population
    def select(self, data: Dict[str, float], generation: int = -1) -> None:
        ids: List[str] = list(sorted(data, key=data.get, reverse=True))

        # Remove a POPGAP fraction of teams
        remainingTeamsCount: int = int(Parameters.POPGAP * len(ids))
        ids = ids[:remainingTeamsCount]

        for team in self.teamPopulation:
            if team.id not in ids and team.referenceCount == 0:
                print(f"REMOVED team {team.id} after generation {generation}. It had {team.referenceCount} references")
                self.teamPopulation.remove(team)

        # Clean up, if there are programs that are not referenced by any teams.
        # Remove them
        self.cleanProgramPopulation() 

    # Create new teams cloned from the remaining root teams
    def evolve(self) -> None:
        while len(self.getRootTeams()) < Parameters.POPULATION_SIZE:
            team = random.choice(self.getRootTeams()).copy()
            Mutator.mutateTeam(self.programPopulation, self.teamPopulation, team)
            self.teamPopulation.append(team)
