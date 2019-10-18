import networkx as nx 
import course_block

def conflict(course_block, other_block):
    if (len(set(course_block.get_day_list()).intersection(set(other_block.get_day_list()))) > 0):
        if (len((set(course_block.get_time_range()).intersection(set(other_block.get_time_range())))) > 0 ):
            if (course_block.course_code[:3] == other_block[:3]):
                return True
    return False


def buildGraph(all_blocks):
    block_graph = nx.DiGraph()
    block_graph.add_nodes_from(all_blocks)

    for node in block_graph:
        for other_node in block_graph:
            if(not conflict(node, other_node)):
                break
                
            




def getOptimal(subject_list):
    return 0