# TO DO:
# DONE -- Chart: Team's reward over time (stacked line chart)
# Chart: Number of teams per champion model (Number of teams vs. generation)
# Chart: Stacked line chart of operation instructions vs. generation 
# Chart: Histogram of operation instructions at a given generation
# Chart: Proportion of state spaced indexed by champion vs. generation

from team import Team

import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.axes import Axes
import seaborn as sns

class Statistics:
    
    reward_df = pd.DataFrame()
    reward_df.columns.name = 'Generation'
    reward_df.index.name = 'Team'

    instruction_df = pd.DataFrame(columns=['+','-','*','/','COS','NEGATE'])
    
    def recordPerformance(self, team: Team, generation: int, score: float):
        self.reward_df.loc[team.id, generation] = score

    def recordInstructionBreakdown(self, team: Team, generation: int):
        for program in team.programs:
            for instruction in program.instructions:
                if team.id not in self.instruction_df.index:
                    self.instruction_df.loc[team.id] = 0
                else:
                    self.instruction_df.loc[team.id, instruction.operation] += 1
                    
    def getInstructionDistributionViolinPlot(self):
        aggregate_df = self.instruction_df.agg(['sum'])

        aggregate_df = aggregate_df.transpose().reset_index()
        aggregate_df.columns = ['Operation', 'Count']

        # Plot violin plot
        fig, ax = plt.subplots()

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
        
        sns.barplot(x='Operation', y='Count', data=aggregate_df, color='white', edgecolor='black', linewidth=2)
        plt.title('Distribution of Operations Across All Teams')
        plt.xlabel('')
        plt.ylabel('Count')

        return plt.gca()
    
        
    def getRewardsVersusTime(self):
        data = self.reward_df.fillna(0)
        data = data.T
        fig, ax = plt.subplots()
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
        ax.legend().remove()  # Removing legend
        return fig

    def getInstructionHistogram(self):
        print (self.instruction_df.head())
        return
        
# Per generation, I'd like to know the reward for all teams.


# Per generation, I'd like to know the number of teams in the champion model.

# Per generation, I'd like to see a histogram of instruction break-down for a team.
