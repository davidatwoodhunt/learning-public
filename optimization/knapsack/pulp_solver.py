from pulp import LpProblem, LpVariable, LpMaximize, lpSum, value
from collections import namedtuple
from typing import List, Tuple
from dataclasses import dataclass
Item = namedtuple("Item", ['index', 'value', 'weight','density'])

def knapsack_problem(capacity, items):
    # Create the problem instance
    problem:LpProblem = LpProblem("Knapsack Problem", LpMaximize)

    # Define the decision variables
    x = [LpVariable(f"x{i}", cat="Binary") for i in range(len(items))]

    # Set the objective function
    problem += lpSum([x[i] * items[i].value for i in range(len(items))])

    # Set the capacity constraint
    problem += lpSum([x[i] * items[i].weight for i in range(len(items))]) <= capacity

    # Solve the problem
    problem.solve()

    # Extract the solution
    selected_items = []
    for i in range(len(items)):
        if value(x[i]) > 0.5:
            selected_items.append(items[i])
    selected_items = [1 if x.index in [s.index for s in selected_items] else 0 for x in items]
    return problem.objective.value(),selected_items

def solve_it(input_data):
    # Modify this code to run your optimization algorithm

    # parse the input
    lines = input_data.split('\n')

    firstLine = lines[0].split()
    item_count = int(firstLine[0])
    capacity = int(firstLine[1])

    items = []
    for i in range(1, item_count+1):
        line = lines[i]
        parts = line.split()
        items.append(Item(i-1, int(parts[0]), int(parts[1]), float(int(parts[0])/int(parts[1]))))

    optimal_value,selected = knapsack_problem(capacity=capacity,items=items)
    # prepare the solution in the specified output format
    #optimal_value, selected = solver_dp_table(capacity=capacity,items = items)
    output_data = str(int(optimal_value)) + ' ' + str(1) + '\n'
    output_data += ' '.join(map(str, selected))
    return output_data