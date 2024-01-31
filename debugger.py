from typing import List
from program import Program
from team import Team
import networkx as nx
import matplotlib.pyplot as plt

class Debugger:

    """ Returns a screenshot of the Tangled Program Graph """
    def screenshot(self, programPopulation: List[Program], teamPopulation: List[Team]):

        G = nx.Graph()

        for team in teamPopulation:
            G.add_node(team.id, node_type="team")

            for program in team.programs:
                if program.action in ["LEFT", "RIGHT"]:
                    G.add_node(program.id, label=program.action, node_type="program")
                    G.add_edge(team.id, program.id, edge_type="team_program")
                else:
                    G.add_edge(team.id, program.action, edge_type="team_team")
                    
        pos = nx.nx_agraph.graphviz_layout(G, prog="sfdp")

        node_labels = nx.get_node_attributes(G, 'label')
        node_types = nx.get_node_attributes(G, 'node_type')
        edge_types = nx.get_edge_attributes(G, 'edge_type')
        
        # Identify connected components (disjoint subgraphs)
        subgraphs = list(nx.connected_components(G))
        
        # Plot each disjoint subgraph separately
        for subgraph_nodes in subgraphs:
            subgraph = G.subgraph(subgraph_nodes)
            
            # Draw team vertices with a black outline
            team_nodes = [node for node in subgraph_nodes if node_types[node] == "team"]
            nx.draw_networkx_nodes(subgraph, pos, nodelist=team_nodes, node_size=700, node_color='white', edgecolors='black', linewidths=2, node_shape='o')
            
            # Draw program vertices as text labels
            program_nodes = [node for node in subgraph_nodes if node_types[node] == "program"]
            nx.draw_networkx_labels(subgraph, pos, labels={node: node_labels[node] for node in program_nodes}, font_size=10, font_family="sans-serif")

            # Draw edges
            team_program_edges = [(u, v) for u, v, data in subgraph.edges(data=True) if data['edge_type'] == "team_program"]
            team_team_edges = [(u, v) for u, v, data in subgraph.edges(data=True) if data['edge_type'] == "team_team"]

            nx.draw_networkx_edges(subgraph, pos, edgelist=team_program_edges, edge_color='gray', width=1, alpha=0.7)
            nx.draw_networkx_edges(subgraph, pos, edgelist=team_team_edges, edge_color='red', width=1, alpha=0.7)
            
            plt.show()

    def getInformation(self, programPopulation: List[Program], teamPopulation: List[Program]) -> str:

        output: Str = "PROGRAMS:\n"
        for program in programPopulation:
            output += f"{program.id}: {program.action}\n"

        output += "TEAMS:\n"
        for team in teamPopulation:
            if team.referenceCount == 0:
                output += "ROOT TEAM "
            else:
                output += "TEAM "

            output += f"{team.id}\n"

            for program in team.programs:
                output += f"{program.id}: {program.action}\n"

        return output
