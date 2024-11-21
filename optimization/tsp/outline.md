# Traveling Salesman Problem 
Calculate shortest route for a full tour

$$ minimize \sum_{i \exists n-1}{dist(v_i, v_{i-1}) + dist(v_n,v_0)}$$


## Methodology 

- prelim start by initalizing a dataclass containing each point and the distance of it to all its neghibors
    - at first this will be all the neghibors in the grid, but optimization is to local search it
- After this is done, try k-opt to tune a hyperparameter for k 
- one k opt hyperparam is done, attempt local search using kopt 
- progress to a simulated anealing approcah with a tau hyperparam 
- multithread a smiliulated annealing approcah with multiple restart and randomization

    