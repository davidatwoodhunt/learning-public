import mosek 
from collections import namedtuple
import sys
Item = namedtuple("Item", ['index', 'value', 'weight','density'])


# Define a stream printer to grab output from MOSEK
def streamprinter(text):
    sys.stdout.write(text)
    sys.stdout.flush()

def knapsack_problem(capacity, items):
    # Create the problem instance
    num_items = len(items)
    with mosek.Env() as env:
        with env.Task() as task:
            task.set_Stream(mosek.streamtype.log, streamprinter)

            # Create variables
            task.appendvars(num_items)

            # Set objective coefficients
            values = [x.value for x in items]
            task.putclist(range(num_items), values)

            task.putobjsense(mosek.objsense.maximize)

            # Add capacity constraint
            task.appendcons(1)
            task.putconbound(0, mosek.boundkey.up, 0.0, capacity)
            weights = [x.weight for x in items]
            task.putarow(0, range(num_items), weights)

            # Set variable bounds
            for i in range(num_items):
                task.putvarbound(i, mosek.boundkey.lo, 0, 1)

            # Set variable integrality constraint
            integrality = [mosek.variabletype.type_int] * num_items
            task.putvartypelist(range(num_items), integrality)

            # Solve the problem
            task.optimize()

            # Get the solution status and selected items
            solsta = task.getsolsta(mosek.soltype.itr)
            print(solsta)
            x = task.getxx(mosek.soltype.itr) 
            print(x)



def solve_it_mosek(input_data):
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

if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1:
        file_location = sys.argv[1].strip()
        with open(file_location, 'r') as input_data_file:
            input_data = input_data_file.read()
        print(solve_it_mosek(input_data))
    else:
        print('This test requires an input file.  Please select one from the data directory. (i.e. python solver.py ./data/ks_4_0)')

