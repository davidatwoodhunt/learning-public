#!/usr/bin/python
# -*- coding: utf-8 -*-

from algo_solver import solve_it_algo,solve_it_wp_w_randomization
def solve_it(input_data):
    # Modify this code to run your optimization algorithm

    # parse the input
    output_data = solve_it_wp_w_randomization(input_data)
    # prepare the solution in the specified output format
    

    return output_data


import sys

if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1:
        file_location = sys.argv[1].strip()
        with open(file_location, 'r') as input_data_file:
            input_data = input_data_file.read()
        print(solve_it(input_data))
    else:
        print('This test requires an input file.  Please select one from the data directory. (i.e. python solver.py ./data/gc_4_1)')

