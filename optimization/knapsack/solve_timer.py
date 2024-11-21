#from solver import solve_it
from pulp_solver import solve_it
from mosek_solver import solve_it_mosek
import logging
import os
from functools import wraps
from time import time

def timing(f):
    @wraps(f)
    def wrap(*args, **kw):
        ts = time()
        result = f(*args, **kw)
        te = time()
        print('func:%r args:[%r, %r] took: %2.4f sec' % \
          (f.__name__, args, kw, te-ts))
        return result
    return wrap

@timing
def run(file_location):
    print(f'Running with {file_location}')
    with open(file_location, 'r') as input_data_file:
        input_data = input_data_file.read()
    if not os.path.exists(f'./solution/{file_location.split("/")[-1]}'):
        solution = solve_it_mosek(input_data)
        with open(f'./solution/{file_location.split("/")[-1]}','w+') as f:
            f.write(solution)
    else:
        print('solution exists')
    

if __name__ == "__main__":
    files = [
        './data/ks_4_0',
        './data/ks_30_0',
        './data/ks_50_0',
        './data/ks_300_0',
        './data/ks_400_0',
        './data/ks_1000_0',
        './data/ks_10000_0'
        
    ]

    import glob 
    files = glob.glob('./data/*')
    
    [run(x) for x in files]