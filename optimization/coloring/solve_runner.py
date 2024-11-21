import os
import multiprocessing
import glob
from solver_pulp import solve_it_pulp


def get_unsolved_problems():
    unsolved = []
    sol_path = './solution'
    print(sol_path)
    files = glob.glob('./data/*')
    print(files)
    for f in files:
        if not os.path.exists(os.path.join(sol_path,f.split("/")[-1])):
            unsolved.append(f)
    return unsolved

def worker(file_location,solve_func):
    with open(file_location, 'r') as input_data_file:
        input_data = input_data_file.read()
        with open(file_location, 'r') as input_data_file:
            input_data = input_data_file.read()
        solution = solve_func(input_data)
        with open(f'./solution/{file_location.split("/")[-1]}','w+') as f:
            f.write(solution)
            
def run_and_save(solve_func,cores=3):
    problems = get_unsolved_problems()

    with multiprocessing.Pool(cores) as pool:
        futures =[]
        for p in problems:
            _ =pool.apply_async(worker,args=(p,solve_func))
            futures.append(_)
        [_.get() for _ in futures]
if __name__ == "__main__":
    run_and_save(solve_it_pulp)