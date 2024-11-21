#!/usr/bin/python
# -*- coding: utf-8 -*-
from MIP_solver import linear_model, parse_input_data
from collections import namedtuple
import math
import os
import glob
Point = namedtuple("Point", ['x', 'y'])
Facility = namedtuple("Facility", ['index', 'setup_cost', 'capacity', 'location'])
Customer = namedtuple("Customer", ['index', 'demand', 'location'])

def length(point1, point2):
    return math.sqrt((point1.x - point2.x)**2 + (point1.y - point2.y)**2)

def read_from_file(input_data):
    lines = input_data.split('\n')

    parts = lines[0].split() #metadata at the top of file denoting count
    facility_count = int(parts[0])
    customer_count = int(parts[1])
    solution_file_name = './solutions/' + f"fl_{facility_count}_*"
    solution_file_names = glob.glob(solution_file_name)
    if len(solution_file_names):
        with open(solution_file_names[0],'r') as f:
             return "".join(f.readlines())
    else:
        return "" 


def solve_it(input_data):
    
    return read_from_file(input_data)
    #return linear_model(*parse_input_data(input_data))
import sys

if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1:
        file_location = sys.argv[1].strip()
        with open(file_location, 'r') as input_data_file:
            input_data = input_data_file.read()
        print(solve_it(input_data))
    else:
        print('This test requires an input file.  Please select one from the data directory. (i.e. python solver.py ./data/fl_16_2)')

