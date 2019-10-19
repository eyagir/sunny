import networkx as nx 
import course_block
import matplotlib.pyplot as plt

def conflict(course_block, other_block):
    if (len(set(course_block.get_day_list()).intersection(set(other_block.get_day_list()))) > 0):
        if (len((set(course_block.get_time_range()).intersection(set(other_block.get_time_range())))) > 0 ):
            return True
    if (course_block.course_code[:3] == other_block.course_code[:3]):
        return True
    else: return False


def buildGraph(all_blocks):
    block_graph = nx.Graph()
    block_graph.add_nodes_from(all_blocks)

    for node in list(block_graph):
        for other_node in list(block_graph):
            if(not conflict(node, other_node)):
                block_graph.add_edge(node, other_node)
    return block_graph
    
                
            




def getOptimal(all_blocks, no_courses):
    full_graph = buildGraph(all_blocks)
    cliques = list(nx.find_cliques(full_graph))
    #for c in list(cliques):
    #    if (len(c) < no_courses):
    #        cliques.remove(c)
    
    cliques.sort(key=custom_sort)

    return cliques


def custom_sort(block_list):
    num_rated = 0
    sum_ratings = 0.00
    for block in block_list:
        num_rated += 1
        sum_ratings += block.rating if block.rating > 0 else 2.5
    if (num_rated >0 ):
        return sum_ratings/num_rated
    else: return 0
