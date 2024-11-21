use std::env;

use std::process;

use tsp_rust::{Config,parse_problem_file, 
                    k_opt,format_solution,
                    compare_prev_and_write_to_file,
                    simulated_annealing};

fn main() {
    let args: Vec<String> =  env::args().collect();
    let config = Config::build(&args).unwrap_or_else(|err|{
        println!("Could not parse args {err}");
        process::exit(1)
    });
    let points = parse_problem_file(&config).unwrap();
    let solution  = simulated_annealing(points,100.0,0.97,300_000);
    let formatted = format_solution(&solution);
    
    println!("{formatted}");
    compare_prev_and_write_to_file(&config,&solution);

}
