## defined solution
import numpy as np
from collections import namedtuple
from dataclasses import dataclass
from typing import List, Tuple
import logging
import random
from queue import PriorityQueue
import multiprocessing
logging.basicConfig(level=logging.INFO,format='[%(asctime)s] %(levelname)-8s %(message)s',)


@dataclass
class Node:
    index: int  # index
    color: int  # color
    degree: int  # humber of connections
    neighbors: List[int]  # neghibors

    def __eq__(self, other):
        if isinstance(other, Node):
            return self.index == other.index
        elif isinstance(other, int):
            return self.index == other
        return False


def calc_degree(node: int, edges: List[Tuple[int,int]]):
    """
    Function to calc degree of a node given list of edges
    """
    # try not to do this iteratively, seems expensive
    # TODO move out
    left, right = zip(*edges)
    node_list = [*left, *right]
    return node_list.count(node)


def assign_neighbors(node: int, edges: List[Tuple[int,int]]):
    """
    Assign the neghibors of the node
    """
    neighbors = []
    for e in edges:
        left, right = e
        if left == node:
            if right not in neighbors:
                neighbors.append(right)
        if right == node:
            if left not in neighbors:
                neighbors.append(left)
    return neighbors


def all_nodes_colored(node_list: List[Node]):
    """
    Boolean return if all nodes are colored in the list
    """
    try:
        sum([x.color for x in node_list])
        return True
    except TypeError:
        return False


def solve_it_algo(input_data):
    """
    attempt using Welsh Powell
    """
    # parse the input
    lines = input_data.split("\n")

    first_line = lines[0].split()
    node_count = int(first_line[0])
    edge_count = int(first_line[1])
    edges = []
    for i in range(1, edge_count + 1):
        line = lines[i]
        parts = line.split()
        edges.append((int(parts[0]), int(parts[1])))
    logging.info("Initalizing node queue")
    nodes = []
    for e in edges:
        index_1, index_2 = e
        if index_1 not in nodes:
            node = Node(
                index_1,
                color=None,
                degree=calc_degree(index_1, edges),
                neighbors=assign_neighbors(index_1, edges),
            )
            nodes.append(node)
        if index_2 not in nodes:
            node = Node(
                index_2,
                color=None,
                degree=calc_degree(index_2, edges),
                neighbors=assign_neighbors(index_2, edges),
            )
            nodes.append(node)
        else:
            pass
    logging.info("Sorting by degree")
    # TODO remember to undo this for output
    random.shuffle(nodes)
    nodes:List[Node] = sorted(nodes, key=lambda x: x.degree, reverse=True,)
    #for n in nodes:
    #    print(n)
    #print("\n")
    colored_nodes = []  # start empty
    color_itr = 0
    logging.info('Optimizing')
    while len(nodes):
        higest_degree_node = nodes[0]
        selected_color = color_itr
        higest_degree_node.color = selected_color
        color_itr += 1
        colored_nodes.append(higest_degree_node)
        for n in nodes[1:]:
            #color all non connected nodes same color
            if higest_degree_node.index not in n.neighbors:
                can_color = True
                for negh in n.neighbors:
                    if negh in [x.index for x in colored_nodes]:
                        if colored_nodes[colored_nodes.index(negh)].color ==selected_color:
                            can_color= False
                        else:
                            pass
                if can_color:
                    n.color = selected_color
                    colored_nodes.append(n)
                    nodes.remove(n)
        nodes.remove(higest_degree_node)
    colored_nodes = sorted(colored_nodes, key=lambda x: x.index, reverse=False)
    color_select = [x.color for x in colored_nodes]
    #for n in colored_nodes:
    #    print(n)
    obj = len(set(color_select))
    
    return obj,color_select


def worker(p,input_data,results):
    '''
    handle running opt
    '''
    logging.info(f'Applying for pass {p}')
    results[p] = solve_it_algo(input_data)
    logging.info('Done')

def solve_it_wp_w_randomization(input_data,passes=100):
    
    manager = multiprocessing.Manager()
    results = manager.dict()
    cpu_count = multiprocessing.cpu_count()

    with multiprocessing.Pool(cpu_count) as pool:
        futures = []
        for p in range(passes):
            _ = pool.apply_async(worker,args=(p,input_data,results))
            futures.append(_)
        [x.get() for x in futures]
    #want min value
    res_d = dict(results)
    values = res_d.values()
    objs, sols = zip(*values)
    obj_min = min(objs)
    idx = objs.index(obj_min)
    return format_solution(obj_min,sols[idx])
def format_solution(obj,color_select):
    output_data = str(obj) + ' ' + str(1) + '\n'
    output_data += ' '.join(map(str, color_select))
    return output_data

import sys

if __name__ == "__main__":
    import sys

    if len(sys.argv) > 1:
        file_location = sys.argv[1].strip()
        with open(file_location, "r") as input_data_file:
            input_data = input_data_file.read()
        sol = solve_it_wp_w_randomization(input_data)
        print(sol)
        f_name = file_location.split('/')[-1]
        print(f_name)

        with open(f'./solution/{f_name}','w+') as f:
           f.write(sol) 
    else:
        print(
            "This test requires an input file.  Please select one from the data directory. (i.e. python solver.py ./data/gc_4_1)"
        )
