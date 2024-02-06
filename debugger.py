from program import Program
from parameters import Parameters
from model import Model

from typing import List
import networkx as nx
import matplotlib.pyplot as plt

import uuid

class Debugger:

	def screenshot(self, model: Model):
		G = nx.Graph()

		def process_team(team):
			visited.add(str(team.id))

			# Add team as a node with a different color and black outline
			G.add_node(team.id, color='white', node_type='team', edgecolor='black', linewidth=2)

			for program in team.programs:
				# Add program as a node with custom shape and different color
				G.add_node(program.id, shape='{}', color='lightgray', node_type='program')

				if program.action in Parameters.ACTIONS:
					actionId: str = str(uuid.uuid4())
					G.add_edge(team.id, program.id) 
					G.add_node(actionId, color='white', node_type='action', label=program.action)
					G.add_edge(program.id, actionId)
				else:
					for childTeam in model.teamPopulation:
						if str(childTeam.id) == program.action and str(childTeam.id) not in visited:
							G.add_edge(team.id, childTeam.id, label="BRYCEBRYCEBRYCE", color='red', linewidth=2.5)  # Connect team to referenced team
							process_team(childTeam)

		visited = set()

		for team in model.getRootTeams():
			if str(team.id) not in visited:
				process_team(team)

		pos = nx.spring_layout(G, k=0.5)
		labels = nx.get_edge_attributes(G, 'label')
		node_colors = [G.nodes[node]['color'] for node in G.nodes]
		edge_colors = [G.nodes[node]['edgecolor'] if G.nodes[node]['node_type'] == 'team' else 'none' for node in G.nodes]
		linewidths = [G.nodes[node]['linewidth'] if G.nodes[node]['node_type'] == 'team' else 0 for node in G.nodes]
		node_shapes = nx.get_node_attributes(G, 'shape')
		node_types = nx.get_node_attributes(G, 'node_type')

		# Set different node sizes for team and program nodes
		node_size = [700 if node_types[node] == 'team' else 350 for node in G.nodes]

		# Use label=None to remove labels for program nodes
		labels_dict = {node: '' if node_types[node] == 'program' or node_types[node] == 'action' else node for node in G.nodes}


		nx.draw(G, pos, with_labels=True, labels=labels_dict, node_size=node_size,
				node_color=node_colors, edgecolors=edge_colors, linewidths=linewidths, font_size=8)

		# Manually draw action nodes with text label
		action_nodes = [node for node in G.nodes if G.nodes[node]['node_type'] == 'action']
		for action_node in action_nodes:
			bbox_props = dict(boxstyle="round,pad=0.3", fc="white", ec="black", alpha=0.7, lw=1)  # Adjust the boxstyle and other parameters as needed
			plt.text(pos[action_node][0], pos[action_node][1], G.nodes[action_node]['label'], ha='center', va='center', color='black', size=6, bbox=bbox_props)

		# Manually draw program nodes with custom shape
		program_nodes = [node for node in G.nodes if G.nodes[node]['node_type'] == 'program']
		for program_node in program_nodes:
			plt.text(pos[program_node][0], pos[program_node][1], G.nodes[program_node]['shape'], ha='center', va='center', color='black', size=8)

		# Draw a legend for node types
		team_legend = plt.Line2D([0], [0], marker='o', color='w', label='Team', markerfacecolor='white', markersize=10, markeredgecolor='black', linewidth=2)
		program_legend = plt.Line2D([0], [0], marker='', color='w', label='Program', markerfacecolor='lightblue', markersize=10)
		plt.legend(handles=[team_legend, program_legend])

		plt.show()
		
	def getInformation(self, model: Model) -> str:

		output: Str = "PROGRAMS:\n"
		for program in model.programPopulation:
			output += f"{program.id}: {program.action}\n"

		output += "TEAMS:\n"
		for team in model.teamPopulation:
			if team.referenceCount == 0:
				output += "ROOT TEAM "
			else:
				output += "TEAM "

			output += f"{team.id}\n"

			for program in team.programs:
				output += f"{program.id}: {program.action}\n"

		return output
