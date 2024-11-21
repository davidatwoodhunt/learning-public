#### solving the graph coloring problem 
import pulp
from collections import Counter
import math 
import mosek

def solve_it_pulp(input_data):
    # parse the input
    lines = input_data.split('\n')

    first_line = lines[0].split()
    node_count = int(first_line[0])
    edge_count = int(first_line[1])

    edges = []
    for i in range(1, edge_count + 1):
        line = lines[i]
        parts = line.split()
        edges.append((int(parts[0]), int(parts[1])))
    #print(edges)
    # Color set to real int nums 
    problem = pulp.LpProblem("GraphColoring",pulp.LpMinimize) ## minimize set of colors 
    #decision variables are the colors of each node
    nodes  = range(node_count)
    #max out number of colors
   #colors = range(min(node_count,math.ceil(math.log(node_count)*5)))
    colors = range(node_count)
    variables = pulp.LpVariable.dicts("NodeColor",(nodes,colors),cat='Binary')
    #objective function
    # maximize the minimum number of colors 
    # array of colors to indicate which ones were used
    used_colors = pulp.LpVariable.dicts("used", colors,cat='Binary')

    # Objective function: minimize the maximum color used (i.e., maximize the sum of colors)
    problem += pulp.lpSum(used_colors[c] for c in colors)

    for n in nodes:
        name = f'{n}_unique_constraint'
        problem += pulp.lpSum([variables[n][c] for c in colors]) == 1,name
    # each node must be a diff color 
    for _, e in enumerate(edges):
        node1 = e[0]
        node2 = e[1]
        for c in colors:
            neq_constraint_name = f'{node1}_{node2}_{c}_inequality_constraint'
            problem += variables[node1][c] + variables[node2][c] <=1,neq_constraint_name
        #problem += pulp.lpSum([variables[node1][c] + variables[node2][c] for c in colors]) == 2
    
    ## node color is a used color
    for n in nodes:
        for c in colors:
            problem += variables[n][c] <= used_colors[c]
    #for c in colors:
    #    problem += pulp.lpSum(variables[n][c] for n in nodes) == used_colors[c]
    #introduce symmetry breaking constraint 

    problem += pulp.lpSum(used_colors[c] for c in colors) <= node_count,"maxColorConstraint"

    #force largest
    # arc tan modifer 
    #fix color of the largest node
    node_size_d = {v:k for k,v in Counter([x[0] for x in edges] + [x[1] for x in edges]).items()}
    # hard coded nodes will get larger as number of nodes increases
    quarter_node = range(math.ceil((math.atan(node_count) * (node_count/100))))
    for _,n in enumerate(quarter_node):
        problem += pulp.lpSum(variables[max(node_size_d)][c] for c in colors) == used_colors[_]
        del node_size_d[max(node_size_d)]
    #break symmetry by forcing 
    #solve
    #solver = pulp.getSolver('MOSEK',MSK_DPAR_MIO_MAX_TIME=1)
    solver = pulp.MOSEK(mip=True,options={'MSK_DPAR_MIO_MAX_TIME':60*60*2}) # 2hr
    #solver = pulp.PULP_CBC_CMD(timeLimit=60*60)
    problem.solve(solver)
    color_select = []
    solution_d = {}
    if problem.status == pulp.LpStatusOptimal:
        for n in nodes:
            for c in colors:
                if pulp.value(variables[n][c]) ==1:
                    color_select.append(c)
                    solution_d[n] = c
        #print(set(color_select))
        obj = int(pulp.value(problem.objective.value()))
        output_data = str(obj) + ' ' + str(1) + '\n'
        output_data += ' '.join(map(str, color_select))
        return output_data
    else:
        raise Exception('Probelm is infeasable')
import sys

if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1:
        file_location = sys.argv[1].strip()
        with open(file_location, 'r') as input_data_file:
            input_data = input_data_file.read()
        print(solve_it_pulp(input_data))
    else:
        print('This test requires an input file.  Please select one from the data directory. (i.e. python solver.py ./data/gc_4_1)')

