import pulp 
import sys
import pandas as pd 
import numpy as  np
from collections import namedtuple
import math
import logging
from typing import Tuple,List

import os
logging.basicConfig(level=logging.INFO)
Point = namedtuple("Point", ['x', 'y'])
Facility = namedtuple("Facility", ['index', 'setup_cost', 'capacity', 'location'])
Customer = namedtuple("Customer", ['index', 'demand', 'location'])

def length(point1, point2):
    return math.sqrt((point1.x - point2.x)**2 + (point1.y - point2.y)**2)


def parse_input_data(input_data:str) -> Tuple[List[Facility],List[Customer]]:
    # parse the input
    lines = input_data.split('\n')

    parts = lines[0].split() #metadata at the top of file denoting count
    facility_count = int(parts[0])
    customer_count = int(parts[1])
    
    facilities = []
    for i in range(1, facility_count+1):
        parts = lines[i].split()
        facilities.append(Facility(i-1, float(parts[0]), int(parts[1]), Point(float(parts[2]), float(parts[3])) ))

    customers = []
    for i in range(facility_count+1, facility_count+1+customer_count):
        parts = lines[i].split()
        customers.append(Customer(i-1-facility_count, int(parts[0]), Point(float(parts[1]), float(parts[2]))))

    return facilities,customers

def generate_distance_map(facilities:List[Facility],customers:List[Customer]) -> dict:
    """
    Generates the lookups for distance based on location of each facility to customer
    TODO: an optimization would be to have a cutoff distance, compute then discard
         if too far since that is nearly guaranteed to be suboptimal 

    input: List[Facility] list of facilities
    customers: List[Customer] list of customers 
    output: dict of facility wtih list of customer distances
    """
    res = {}
    for f in facilities: # assuming sorted by index
        distances = []
        for c in customers: #Core assumption is that its sorted by index
            distances.append(length(f.location,c.location))
        res[f.index]= distances
    return res

def save_output_string(file_location:str,output_data:str,replace=False) ->None:
    """
    Save to text if doesn't exist
    """
    f_name = file_location.split("/")[-1]
    logging.info(f'saving solution')
    f_path = f'./solutions/{f_name}'
    if not os.path.exists(f_path) or replace:
        with open(f_path,'w+') as f:
            f.write(output_data)


def linear_model(facilities:List[Facility],customers:List[Customer]) -> str:
    """
    Solver for the facility problem input in the form of facilities and customers
    output is the result of the model wiht the cost + optimality proof toggle 
    followed by mapping of customer to facility in customer index order 
    
    """

    logging.info(f'Computing distances')
    distances = generate_distance_map(facilities,customers)
    logging.info(f'done')

    prob = pulp.LpProblem('Facility',pulp.LpMinimize)
    #set up variables 
    facility_selection = pulp.LpVariable.dicts("facility",[(f.index,c.index) for f in facilities for c in customers],cat=pulp.LpBinary)
    #objective min cost constrainted on set up costs etc
    # objective function will be on the order of min fixed + varaible costs per customer constrained on each customer has a facility
    #variable cost is the eculidian distance between locations
    #compute once
    logging.info('Setting up Objective')

    obj = pulp.lpSum(
                pulp.lpSum(
                        (facility_selection[f.index,c.index] * facilities[f.index].setup_cost) + 
                        (facility_selection[f.index,c.index] * distances[f.index][c.index])
                                 for c in customers ) 
                                    for f in facilities)
    prob += obj
    logging.info('Setting up Constraints')
    #subject to customer constraints
    for c in customers:
        prob += pulp.lpSum(facility_selection[f.index,c.index] for f in facilities) ==1  #only one customer per

    #subject to capcacity constraints
    for f in facilities:
        prob += pulp.lpSum(facility_selection[f.index,c.index] * c.demand for c in customers) <= facilities[f.index].capacity 

    solver = pulp.MOSEK(options={"MSK_DPAR_MIO_TOL_ABS_GAP": 0.02})
    prob.solve(solver)
    if pulp.LpStatus[prob.status] == "Optimal":
        print('Optimal')
        res = f"{prob.objective.value()} 1 \n"
        for f in facilities:
            for c in customers:
                if facility_selection[f.index,c.index].value() == 1:
                    print(f'Selected facility {f.index} for customer {c.index}')
                    res += f"{f.index} "
        return res
    else:
        print("not feasiblie")
        return ""
    

def main():

    if len(sys.argv) > 1:
        file_location = sys.argv[1].strip()
        with open(file_location, 'r') as input_data_file:
            input_data = input_data_file.read()
        facilities, customers = parse_input_data(input_data)
        #print(facilities)
        #print("*"*300)
        #print(customers)

        output = linear_model(facilities,customers)
        save_output_string(file_location,output)
        print(output)
    else:
        print('This test requires an input file.  Please select one from the data directory. (i.e. python solver.py ./data/fl_16_2)')


def run_all_examples():
    examples = ['./data/fl_25_2',
                './data/fl_50_6',
                './data/fl_100_7', 
                './data/fl_100_1',
                './data/fl_200_7', 
                './data/fl_500_7', 
                './data/fl_1000_2', 
                './data/fl_2000_2',
                ]
    for file_location in examples:
        with open(file_location, 'r') as input_data_file:
            input_data = input_data_file.read()
        facilities, customers = parse_input_data(input_data)
        output = linear_model(facilities,customers)
        save_output_string(file_location,output)
        print(output)

if __name__ == '__main__':
    main()
    #run_all_examples()