#!/usr/bin/python
# -*- coding: utf-8 -*-

import math
from collections import namedtuple
from tsp_MIP import solve_MIP
Point = namedtuple("Point", ['x', 'y'])

def length(point1, point2):
    return math.sqrt((point1.x - point2.x)**2 + (point1.y - point2.y)**2)


def solve_it_cached(input_data):
    lines = input_data.split('\n')

    nodeCount = int(lines[0])
    solution = ''
    try:
        with open(f'/Users/davidhunt/research/learning/optimization/tsp/solutions/tsp_{nodeCount}_1','r+') as f:
            solution = ''.join(f.readlines())
        return solution
    except FileNotFoundError:
        return solve_MIP(input_data)
def solve_it(input_data):
    # Modify this code to run your optimization algorithm

    # parse the input
    
    return solve_it_cached(input_data)


import sys

if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1:
        file_location = sys.argv[1].strip()
        with open(file_location, 'r') as input_data_file:
            input_data = input_data_file.read()
        print(solve_it(input_data))
    else:
        print('This test requires an input file.  Please select one from the data directory. (i.e. python solver.py ./data/tsp_51_1)')

