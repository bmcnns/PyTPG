# TO DO:
# DONE -- Chart: Team's reward over time (stacked line chart)
# Chart: Number of teams per champion model (Number of teams vs. generation)
# Chart: Stacked line chart of operation instructions vs. generation 
# Chart: Histogram of operation instructions at a given generation
# Chart: Proportion of state spaced indexed by champion vs. generation

from team import Team
from environment import Environment
from debugger import Debugger

import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.axes import Axes
import seaborn as sns

class Statistics:
	
	reward_df = pd.DataFrame()
	reward_df.columns.name = 'Generation'
	reward_df.index.name = 'Team'

	instruction_df = pd.DataFrame(columns=['+','-','*','/','COS','NEGATE'])

	def reset(self):
		self.instruction_df = pd.DataFrame(columns=['+','-','*','/','COS','NEGATE'])
	
	def recordPerformance(self, team: Team, generation: int, score: float):
		self.reward_df.loc[team.id, generation] = score

	def recordInstructionBreakdown(self, team: Team, generation: int):
		for program in team.programs:
			for instruction in program.instructions:
				if team.id not in self.instruction_df.index:
					self.instruction_df.loc[team.id] = 0
				else:
					self.instruction_df.loc[team.id, instruction.operation] += 1
					
	def getInstructionDistributionViolinPlot(self, ax):
		aggregate_df = self.instruction_df.agg(['sum'])

		aggregate_df = aggregate_df.transpose().reset_index()
		aggregate_df.columns = ['Operation', 'Count']

		sns.set_palette("gray")
		
		operation_labels = {
			'+': 'ADDITION',
			'-': 'SUBTRACTION',
			'*': 'MULTIPLICATION',
			'/': 'DIVISION',
			'COS': 'COS',
			'NEGATE': 'NEGATE'
		}

		aggregate_df['Operation'] = aggregate_df['Operation'].map(operation_labels)
		
		sns.barplot(x='Operation', y='Count', data=aggregate_df, color='white', edgecolor='black', linewidth=2, ax=ax)
		ax.set_title('Distribution of Operations Across All Teams')
		ax.set_xlabel('')
		ax.set_ylabel('Count')

	def getRewardsVersusTime(self, ax):
		data = self.reward_df.fillna(0)
		data = data.T
		colors = ['black'] * len(data.columns)  # Setting line color to black for all lines

		for col in data.columns:
			ax.plot(data.index, data[col], linestyle=':', marker='x', color='black')  # Using 'x' marker and black color
			# Displaying labels for top 3 performing teams
		max_values = data.iloc[-1].nlargest(3)
		top_teams = max_values.index
		
		for team in top_teams:
			max_val = max_values[team] 
			max_index = data.index[-1]
			ax.text(max_index, max_val, team, ha='center', va='bottom', color='black', fontsize=10)

		ax.set_xlabel('Generation')
		ax.set_ylabel('Cumulative Reward')

		ax.set_title('Cumulative rewards of teams over time')

	def save(self, environment: Environment, generation, team, teamPopulation, step):
		fig, axs = plt.subplots(2, 2, figsize=(10,8))
		axs = axs.flatten()
		self.getInstructionDistributionViolinPlot(axs[0])
		self.getRewardsVersusTime(axs[1])
		environment.display(axs[2], generation, team, step)
		Debugger.plotTeam(team, teamPopulation, axs[3])
		plt.tight_layout()
		plt.savefig("bin/plot.png")
		plt.close(fig)
		# Per generation, I'd like to know the reward for all teams.

# Per generation, I'd like to know the number of teams in the champion model.

# Per generation, I'd like to see a histogram of instruction break-down for a team.
