import numpy as np 
import math
from dataclasses import dataclass
from typing import List
import logging
import sys
import multiprocessing
logging.basicConfig(level=logging.INFO,format='[%(asctime)s] %(levelname)-8s %(message)s')

@dataclass
class Point:
    index: int
    x: float
    y: float

    def __hash__(self) -> int:
        return hash(f'{self.x}_{self.y}')

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

def length(point1, point2):
    return math.sqrt((point1.x - point2.x)**2 + (point1.y - point2.y)**2)

def plot_solution(points:List,file_location):
    import matplotlib.pyplot as plt 
    
    x = [x.x for x in points]
    y = [x.y for x in points]
    fig = plt.figure(figsize=(10, 10))
    fig.clear()
    plt.scatter(x=x,y=y)

    for _ in range(len(points)-1):
        p = points[_]
        n = points[_+1]
        plt.annotate( "", xytext=(p.x,p.y), xy=(n.x, n.y),
              arrowprops=dict( arrowstyle="->" ) )
    plt.annotate( "", xytext=(points[-1].x,points[-1].y), xy=(points[0].x, points[0].y),
              arrowprops=dict( arrowstyle="->" ) )
    f_name = file_location.split("/")[-1]
    
    logging.info(f'saving plot')

    plt.savefig(f'./plots/{f_name}.png')


def get_k_nearest(tour:List,k=6):
    '''
    Returns k nearest solutions to node
    '''
    sub_solutions = []
    for i in range(k):
        #random select k-opt
        k_param = np.random.choice([2,3])
        sub_solutions.append(swap(tour.copy(),k=k_param))
    return sub_solutions

def format_solution(tour:List,file_location):
    #start at index 0 and go from there 
    fmat = [x.index for x in tour]
    obj = calc_tour_length(tour)
    output_data = '%.2f' % obj + ' ' + str(1) + '\n'
    output_data += ' '.join(map(str, fmat))

    f_name = file_location.split("/")[-1]
    
    logging.info(f'saving solution')

    with open(f'./solutions/{f_name}','w+') as f:
         f.write(output_data)
        
    return  output_data
    
def calc_tour_length(tour:List[Point]) ->float:
    '''
    returns the length of the tour
    
    '''
    obj = 0
    for _ in range(len(tour)-1):
        obj += length(tour[_],tour[_+1])
    obj += length(tour[-1],tour[0])
    return obj
    
def swap(tour:List[Point],k) ->List[Point]:
    '''
    Perform point swap
    '''
    for _ in range(k):
        #select random sampled 
        selected = np.random.choice(tour,k)
        sorted(selected,key=lambda x: x.index) #maintain order
        indices = [x.index for x in selected]
        #fix direction
        tour[indices[0]:indices[-1]+1] = reversed(tour[indices[0]:indices[-1]+1])
    return tour

def k_opt(initial_tour,k=2,iterations=10000,file_location=None):
    '''
    Perform k--opt
    '''
    best_tour = initial_tour 
    best_tour_length = calc_tour_length(initial_tour)
    iterations *= len(initial_tour)
    cuts_wo_improvement = 0
    cutoff = iterations * np.log(len(initial_tour))

    for _ in range(iterations):
        if _ %1000 == 0:
            logging.info(f'On Cut: {_//1000}k')
        new_tour = swap(best_tour.copy(),k)
        new_tour_length = calc_tour_length(new_tour)
        if new_tour_length < best_tour_length:
            best_tour = new_tour
            best_tour_length = new_tour_length
            ##temp
            ##plot_solution(new_tour,file_location=file_location)
            cuts_wo_improvement = 0
        else:
            cuts_wo_improvement +=1
        if cuts_wo_improvement > cutoff:
            logging.info('No Noticible improvement found within cutoff')
            break
    return best_tour

def simulated_annealing(initial_tour,max_temp=100,alpha=.95,iterations = 1000,file_location=None):
    '''
    Run Simulated annealing algo
    '''
    
    system_temp = max_temp
    best_tour = initial_tour
    best_cost = calc_tour_length(best_tour)
    #set reheats
    cycles_wo_improvement = 0
    reheats = 0
    CYCLE_CUT = np.log(len(initial_tour)) *5
    MAX_REHEATS = 0 # max number of reheat cycles
    REHEAT_MODIFER = 10 #double sys temp
    while system_temp >0.01:
        n_pass = 0
        improvement = False
        while n_pass < iterations:
            #compute cost swap
            if reheats == MAX_REHEATS:
                #hit our limit, go to 2 
                new_tour = swap(best_tour.copy(),k=2)
            else:
                new_tour = swap(best_tour.copy(),k=3)
            new_cost = calc_tour_length(new_tour)
            if new_cost < best_cost:
                #accept it 
                best_tour = new_tour
                best_cost = new_cost
                improvement = True
                cycles_wo_improvement =0

            activation_value = np.exp(-new_cost/system_temp)
            rand_val = np.random.uniform()
            if activation_value >rand_val :
                #Accept some dedgredation
                #logging.info(f'Degrading SOlution {activation_value} {rand_val} || {np.exp(-(new_cost-best_cost)/system_temp)}')
                best_tour = new_tour
                best_cost = new_cost
            n_pass += 1
        if not improvement:
            cycles_wo_improvement +=1
        if (cycles_wo_improvement > CYCLE_CUT) and (reheats < MAX_REHEATS):
            
            system_temp += REHEAT_MODIFER
            reheats += 1
            logging.info(f'System is not converging, reheatting to {system_temp}, {MAX_REHEATS-reheats} left')
            cycles_wo_improvement =0
        #plot_solution(new_tour,file_location=file_location)
        system_temp *= alpha
        logging.info(f'System temp: {system_temp}') 
    return best_tour
        

def tabu_worker(tour_start,tabu,cycle_cutoff,max_tabu):
    best_tour = tour_start
    best_cost = calc_tour_length(best_tour)
    cycles_without_improvement = 0
    while cycles_without_improvement <= cycle_cutoff:
        neghiborhood = get_k_nearest(best_tour)
        for tour in neghiborhood:
            if calc_tour_length(tour) < best_cost:
                if tour not in tabu:
                    best_tour = tour
                    best_cost = calc_tour_length(tour) 
                    tabu.append(tour)
                    cycles_without_improvement = 0
                    #logging.info('Plotting better solution')
                    #plot_solution(tour,file_location=file_location)
            else:
                cycles_without_improvement += 1
        if len(tabu)>=max_tabu:
            tabu.pop(0)
    logging.info(f'Done')
    return best_tour

def tabu_search(initial_tour,cycle_cutoff=200000,file_location=None,max_tabu=100000):
    logging.info('Tabu Search')
    manager = multiprocessing.Manager()
    tabu = manager.list()
    cpu_count = multiprocessing.cpu_count()
    with multiprocessing.Pool(cpu_count) as pool:
        futures = []
        for p in range(cpu_count):
            logging.info(f'Applying pass {p}')
            _ = pool.apply_async(tabu_worker,args=(initial_tour,
                                                   tabu,
                                                   cycle_cutoff,
                                                   max_tabu
                                                   ))
            futures.append(_)
        tours = [x.get() for x in futures]
        costs = [calc_tour_length(x) for x in tours]
    best_tour = tours[costs.index(min(costs))]
    return best_tour

def solve_tsp(input_data,file_location=None):

    points = parse_input_data(input_data) 
    logging.info(f'Initalized {len(points)} point problem')
    logging.info('setting inital state')
    visited_points = []
    remaining_points = set(points)
    current_point = np.random.choice(points)
    visited_points.append(current_point)
    remaining_points.remove(current_point)
    while remaining_points:
        nearest = min(remaining_points,key=lambda x: length(current_point,x))
        remaining_points.remove(nearest)
        visited_points.append(nearest)
        current_point = nearest

    
    #visited_points = k_opt(visited_points,k=3,file_location=file_location)
    #visited_points = simulated_annealing(visited_points,file_location=file_location)
    visited_points = tabu_search(visited_points,file_location=file_location)
    logging.info('Plotting')
    #plot_solution(visited_points,file_location)
    logging.info('done')
    best_tour =  calc_tour_length(visited_points),visited_points
    return format_solution(best_tour[1])

def worker(p,input_data,results,file_location=None):
    logging.info(f'Applying for pass {p}')
    results[p] = solve_tsp(input_data,file_location)
    logging.info('Done')

def solve_tsp_multi_randomization(input_data,file_location=None):
    manager = multiprocessing.Manager()
    results = manager.dict()
    cpu_count = multiprocessing.cpu_count()
    passes = cpu_count
    with multiprocessing.Pool(cpu_count) as pool:
        futures = []
        for p in range(passes):
            _ = pool.apply_async(worker,args=(p,input_data,results,file_location))
            futures.append(_)
        [x.get() for x in futures]
    #want min value
    res_d = dict(results)
    values = res_d.values()
    objs, sols = zip(*values)
    obj_min = min(objs)
    idx = objs.index(obj_min)
    return format_solution(sols[idx])
if __name__ == "__main__":
    import sys

    if len(sys.argv) > 1:
        file_location = sys.argv[1].strip()
        with open(file_location, "r") as input_data_file:
            input_data = input_data_file.read()
        #sol = solve_tsp_multi_randomization(input_data,file_location)
        sol = solve_tsp(input_data,file_location)
        print(sol)
    else:
        print(
            "This test requires an input file.  Please select one from the data directory. (i.e. python solver.py ./data/gc_4_1)"
        )