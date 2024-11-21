from pulp import LpProblem, LpVariable, LpMinimize, lpSum, getSolver, value
import pickle
from collections import namedtuple
from tsp_solve import plot_solution,format_solution
# Define the points
Point = namedtuple("Point", ['index','x', 'y'])


def parse_input_data(input_data) :
     # parse the input
    lines = input_data.split('\n')

    nodeCount = int(lines[0])

    points = []
    index=0
    for i in range(1, nodeCount+1):
        line = lines[i]
        parts = line.split()
        points.append(Point(index,float(parts[0]), float(parts[1])))
        index += 1
    return points

def solve_MIP(input_data,file_location=None):
# Create a distance matrix
    print("Parsing Data")
    cities = parse_input_data(input_data)
    n = len(cities)
    dist_matrix = [[0] * n for _ in range(n)]
    print('Generating cost matrix')
    for i in range(n):
        for j in range(n):
            if i != j:
                dist_matrix[i][j] = ((cities[i].x - cities[j].x) ** 2 + (cities[i].y - cities[j].y) ** 2) ** 0.5

    # Create a PuLP problem
    print('creating pulp')
    tsp_problem = LpProblem("TSP", LpMinimize)

    # Create binary decision variables: x[i][j] is 1 if the path goes from city i to city j
    x = [[LpVariable(f'x_{i}_{j}', cat='Binary') for j in range(n)] for i in range(n)]
    print('adding objective')
    # Objective function: minimize the total distance
    tsp_problem += lpSum(dist_matrix[i][j] * x[i][j] for i in range(n) for j in range(n))
    print('Adding Constraints')
    # Constraints
    for i in range(n):
        tsp_problem += lpSum(x[i][j] for j in range(n) if i != j) == 1  # Each city is visited once
        tsp_problem += lpSum(x[j][i] for j in range(n) if i != j) == 1  # Each city is left once
    print('MTZ constrraint')
    # Additional constraint to prevent sub-tours (Miller-Tucker-Zemlin constraints)
    u = [LpVariable(f'u_{i}', lowBound=0, upBound=n-1, cat='Integer') for i in range(n)]
    for i in range(1, n):
        for j in range(1, n):
            if i != j:
                tsp_problem += u[i] - u[j] + n * x[i][j] <= n - 1
    print('Solving')
    # Solve the problem
    solver = getSolver('MOSEK')
    tsp_problem.solve(solver)

    # Extract the solution
    tour = []
    i = 1
    while len(tour) < n:  # Continue until the tour is of length n
        for j in range( n ):  # Iterate through all nodes (1 to n)
            if value(x[i][j]) == 1:  # Check for the connection
                tour.append(i)
                i = j
                break

    # Print the optimal tour
    print("Optimal Tour:")
    points_tour = []
    for c in tour:
        points_tour.append([x for x in cities if x.index==c][0])
    plot_solution(points_tour,file_location)
    return format_solution(points_tour,file_location)


def run_courseras():
    files = [
        './data/tsp_100_3',
        './data/tsp_200_2',
        './data/tsp_574_1',
        './data/tsp_1889_1',
        './data/tsp_33810_1'
    ]
    for f in files:
        print(f"Running {f}")
        with open(f, "r") as input_data_file:
            input_data = input_data_file.read()
        sol = solve_MIP(input_data,f)
        print(sol)

if __name__ == "__main__":
    import sys

    if len(sys.argv) > 1:
        file_location = sys.argv[1].strip()
        with open(file_location, "r") as input_data_file:
            input_data = input_data_file.read()
        sol = solve_MIP(input_data,file_location)
        print(sol)
    else:
        print(
            "Running all courseras"
        )
        run_courseras()