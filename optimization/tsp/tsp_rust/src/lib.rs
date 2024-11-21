use std::fs;
use std::error::Error;
use rand::seq::SliceRandom;
use std::fmt;
use std::fs::File;
use std::path::Path;
use std::io::Read;
use std::io::Write;
use rand::Rng;
pub struct Config {
    pub file_path: String,
}
impl Config {
    pub fn build(args: &[String]) -> Result< Config, &'static str>{
        if args.len() <2 {
            return Err("No filepath specificed")
        }
        let file_path = args[1].clone();
        Ok(Config{file_path})
    }
}


#[derive(Debug,Clone)]
pub struct Point {
    pub index: usize,
    pub x: f64,
    pub y: f64,
}
impl PartialEq for Point {
    fn eq(&self, other: &Self) -> bool {
        self.index == other.index
        //think implementing this will push the sort order to use index
    }
}
impl fmt::Display for Point {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        write!(f, "{}", self.index)
    }
}

pub fn parse_problem_file(config:&Config) -> Result<Vec<Point>,Box<dyn Error>>{
    let contents = fs::read_to_string(&config.file_path)?;
    let mut points: Vec<Point> = vec![];
    for (i, line) in contents.lines().enumerate(){
        //skip statement about number of items
        if i>0{
            let parsed_line: Vec<&str> = line.split(" ").collect();
            //dbg![&parsed_line];
            points.push(Point{
                index: i-1 ,
                x: parsed_line[0].parse().unwrap(),
                y: parsed_line[1].parse().unwrap()
            })
        }
    }
    //dbg![&points];
    Ok(points)
}

pub fn format_solution(tour: &Vec<Point>) ->String{
    let tour_length = calc_tour_length(tour);

    let format_str = tour.iter().map(|x| x.to_string())
                        .collect::<Vec<String>>()
                        .join(" ");
    //println!("{format_str}");
    let output_string = String::from(format!("{} 1 \n",tour_length)) + &format_str;
    //output_string;
    output_string
}

fn write_to_file(path:&Path, solution_str:String) -> std::io::Result<()> {
    let mut file = File::create(path)?;
    // String to write to the file
    // Write the string to the file
    file.write_all(solution_str.as_bytes())?;
    println!("String written to file.");
    Ok(())
}

pub fn compare_prev_and_write_to_file(config:&Config,tour:&Vec<Point>){
    let path = Path::new(&config.file_path);
    let parent = path.parent();
    if let Some(parent) = parent {
        let grandparent = parent.parent();
        if let Some(grandparent) = grandparent {
            let solution_path = grandparent.join(Path::new(&format!("solutions/{}", path.file_name().unwrap().to_str().unwrap())));
            println!("{}",&solution_path.display());
            if solution_path.exists() && solution_path.is_file(){
                let mut file = match File::open(&solution_path) {
                    Ok(file) => file,
                    Err(_) => {
                        println!("Failed to open the file for reading.");
                        return;
                    }
                };
                // Read the file's contents into a String
                let mut contents = String::new();
                if let Err(_) = file.read_to_string(&mut contents) {
                    println!("Failed to read the file.");
                    return;
                }
                // Process the contents (e.g., print or use them)
                let lines: Vec<&str> = contents.split('\n').collect();
                // Check if there is at least one line
                if let Some(first_line) = lines.first() {
                    let saved_best = first_line.split_whitespace().collect::<Vec<&str>>()[0];
                    match saved_best.parse::<f64>(){
                        Ok(float_value) => {
                            let new_best = calc_tour_length(tour);
                            if new_best < float_value{
                                _ = write_to_file(&solution_path,format_solution(&tour));
                            }

                            else{
                                println!("New Soluton worse, passing");
                            }
                        }
                        Err(err) => {
                            println!("{saved_best}");
                            println!("Error parsing as f64: {:?}", err);
                        }
                    }
                } else {
                    println!("No lines found in the file.");
                }
            }
            else{
                println!("no solution path exists, writing");
                _ = write_to_file(&solution_path,format_solution(&tour));
            }
        }
    }
}


//////// logic for handling tsp 


fn length(point1: &Point, point2: &Point) -> f64 {
    let dx = point1.x - point2.x;
    let dy = point1.y - point2.y;
    
    (dx.powi(2) + dy.powi(2)).sqrt()
}

fn k_swap(tour: &Vec<Point>, k: usize) -> Vec<Point> {
    // Perform point swap k times
    let mut rng = rand::thread_rng();
    let len = tour.len();
    let mut new_tour: Vec<Point> = tour.clone(); // Create a new Vec<Point> with the same elements as tour

    for _ in 0..k {
        // Select k distinct random indices
        let mut indices: Vec<usize> = (0..len).collect();
        indices.shuffle(&mut rng);
        indices.truncate(k);

        // Perform the k-opt swap on the new_tour
        let mut temp_tour = new_tour.clone();
        for i in 0..k {
            let j = k - 1 - i;
            temp_tour[indices[i]] = new_tour[indices[j]].clone();
        }

        new_tour = temp_tour;
    }
    new_tour // Return the new tour
}

fn get_k_nearest(tour: Vec<Point>, k:usize) -> Vec<Vec<Point>>{
    let mut sub_solutions: Vec<Vec<Point>> =vec![vec![]];
    for _ in 0..k{
        sub_solutions.push(k_swap(&tour.clone(),k));
    }
    sub_solutions
}

fn calc_tour_length(tour: &Vec<Point>) -> f64 {
    tour.iter()
        .zip(tour.iter().cycle().skip(1))
        .map(|(p1, p2)| length(p1, p2))
        .sum()
}
use core::cmp::Ordering;
fn initialize_greedy_tour(mut tour:Vec<Point>) ->Vec<Point>{

    let mut new_tour:Vec<Point> = vec![];
    let mut current_point: Option<Point> = None;

    while !tour.is_empty(){
        let nearest = tour.iter().min_by(|&point1, &point2| {
            match &current_point {
                Some(cp) => {
                    length(&cp, point1)
                        .partial_cmp(&length(&cp, point2))
                        .unwrap_or(Ordering::Equal) // Provide a default Ordering if partial_cmp returns None
                }
                None => Ordering::Equal, // Handle the case where current_point is None
            }
        })
        .cloned();

        match nearest{
            Some(nearest_point) =>{
                tour.retain(|point| *point != nearest_point);
                new_tour.push(nearest_point.clone());
                current_point = Some(nearest_point);
            }
            None =>{
                break;
            }
        }
    }
    new_tour
}

use std::f64::consts::E;

pub fn simulated_annealing(initial_tour: Vec<Point>, max_temp: f64, alpha: f64, iterations: u32) -> Vec<Point> {
    let mut system_temp = max_temp;
    println!("Initalizing Greedy tour");
    let mut best_tour = initialize_greedy_tour(initial_tour.clone());
    let mut best_cost = calc_tour_length(&best_tour);
    
    // Set reheats
    let mut cycles_wo_improvement = 0;
    let mut reheats = 0;
    let CYCLE_CUT = ((initial_tour.len() as f64).ln() * 5.0) as u32;
    let MAX_REHEATS = 5; // Max number of reheat cycles
    let REHEAT_MODIFER = 10.0; // Double sys temp
    
    while system_temp > 0.01 {
        let mut n_pass = 0;
        let mut improvement = false;
        
        while n_pass < iterations {
            // Compute cost swap
            let new_tour = k_swap(&best_tour, 2); // Assuming swap function is defined elsewhere
            let new_cost = calc_tour_length(&new_tour);
            
            if new_cost < best_cost {
                // Accept it
                best_tour = new_tour.clone();
                best_cost = new_cost;
                improvement = true;
                
                cycles_wo_improvement = 0;
            }
            else{
                let delta = new_cost - best_cost;
                let activation_value = E.powf(-delta / system_temp);
                let rand_val = rand::thread_rng().gen::<f64>();
                
                if activation_value > rand_val {
                    // Accept some degradation
                    best_tour = new_tour.clone();
                    best_cost = new_cost;
                }
                
            }
            
            n_pass += 1;
        }
        
        if !improvement {
            cycles_wo_improvement += 1;
        }
        
        if cycles_wo_improvement > CYCLE_CUT && reheats < MAX_REHEATS {
            system_temp += REHEAT_MODIFER;
            reheats += 1;
            println!("System is not converging, reheating to {}, {} left", system_temp, MAX_REHEATS - reheats);
            cycles_wo_improvement = 0;
        }
        
        system_temp *= alpha;
        println!("Best Tour: {}",&best_cost);
        println!("System temp: {}", system_temp);
    }
    println!("Running final k_opt");
    let k_opt_tour = k_opt(best_tour,2,iterations);
    k_opt_tour
}

pub fn k_opt(initial_tour: Vec<Point>, k:usize,iterations:u32) -> Vec<Point>{
    // Runs kopt and returns best tour

    let mut best_tour = initial_tour.clone();
    let mut best_tour_length = calc_tour_length(&best_tour);
    let mut cuts_wo_improvement = 0;
    let mut tabu:Vec<Vec<Point>> = vec![initial_tour.clone()];
    for _i in 0..iterations{
        //if _i %1000 ==0{
        //    println!("On cut {}", _i /1000);
        //}
        let mut rng = rand::thread_rng();
        let actual_k = rng.gen_range(1..=k);
        let new_tour = k_swap(&best_tour.clone(),actual_k);
        let new_tour_length = calc_tour_length(&new_tour);

    let intensification_interval = 100; // Adjust this interval
        //println!("{}",new_tour_length);
        if new_tour_length <= best_tour_length{
            if _i % intensification_interval == 0 {
                let intensification_iterations = 50; // Adjust this number
                let mut best_solution_variation = best_tour.clone();
                let mut best_variation_length = best_tour_length;

                for _j in 0..intensification_iterations {
                    let variation = k_swap(&best_tour.clone(), actual_k);
                    let variation_length = calc_tour_length(&variation);

                    if variation_length < best_variation_length {
                        best_solution_variation = variation.clone();
                        best_variation_length = variation_length;
                    }
                }

                if best_variation_length < best_tour_length {
                    best_tour = best_solution_variation.clone();
                    best_tour_length = best_variation_length;
                }
            }
            if !tabu.iter().any(|t| t == &new_tour) {
                 // If it's time for intensification, explore variations of the best solution
                
            
                best_tour = new_tour.clone(); 
                println!("New Best: {:?}", best_tour_length);
                best_tour_length = new_tour_length;
                cuts_wo_improvement = 0;
                tabu.push(new_tour.clone());
            }
            
            
            else{
                //println!("in tabu");
                cuts_wo_improvement += 1;
            }
            //allow for some degredation 
            
            //println!("tabu size: {}",tabu.len());
        }
    
    }
    best_tour
}

pub fn k_opt_all(config:&Config) ->std::io::Result<()>{
    let file_path = Path::new(&config.file_path);
    let entries = fs::read_dir(file_path)?;
    for entry in entries {
        let entry = entry?;
        let path = entry.path();
        println!("{:?}",path);
        // Check if the entry is a file (not a directory)
        if path.is_file() {
            // Print the file name
            if let Some(file_name) = path.file_name() {
                println!("{}", file_name.to_string_lossy());
            }
        }
    }
    Ok(())
}


//// tests 

#[cfg(test)]
mod tests{
    use super::*;
    use std::process;
    #[test]
    fn test_length(){
        let point1 = Point{
            index:0,
            x:10.0,
            y:24.0
        };
        let point2 = Point{
            index:1,
            x:42.0,
            y:100.0
        };
        assert_eq!(82.46211251235322,length(&point1,&point2))
    }

    #[test]
    fn test_swap(){
        let config = Config{file_path:String::from("../data/tsp_5_1")};
        let mut points = parse_problem_file(config).unwrap_or_else(|err|{
            println!("Failed to parse {err}");
            process::exit(1);
        });
        println!("Before: {:?}",&points);
        let before = points.clone();
        let after = k_swap(& points,2);
        println!("After: {:?}",&after);
        assert_ne!(before,after);

    }

    #[test]
    fn test_k_opt(){
        let config = Config{file_path:String::from("../data/tsp_51_1")};
        let mut points = parse_problem_file(config).unwrap_or_else(|err|{
            println!("Failed to parse {err}");
            process::exit(1)
        });
        println!("{} len", calc_tour_length(&points));
        let new_tour = k_swap(&points,2);
        println!("{} len", calc_tour_length(&new_tour));
    }
    #[test]
    fn test_calc_tour_length(){
        let config = Config{file_path:String::from("../data/tsp_5_1")};
        let mut points = parse_problem_file(config).unwrap_or_else(|err|{
            println!("Failed to parse {err}");
            process::exit(1)
        });
        assert_eq!(4.0,calc_tour_length(&points));
        assert_ne!(4.1,calc_tour_length(&points));
    }
}