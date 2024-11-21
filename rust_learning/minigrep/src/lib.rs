
use std::fs;
use std::error::Error;
use std::env;

pub struct Config{
    pub query: String,
    pub file_path: String,
    pub ingore_case: bool,
}
impl Config{
    pub fn build(
        mut args: impl Iterator<Item = String>,
    ) -> Result <Config, &'static str> {
        args.next();

        let query = match args.next(){
            Some(arg) => arg,
            None => return Err("Didn't Get a query string"),
        };
        let file_path = match args.next(){
            Some(arg) => arg,
            None => return Err("Didn't Get a file path")
        };
        let ingore_case = env::var("IGNORE_CASE").is_ok();
        Ok(Config{
            query,
            file_path,
            ingore_case
        })
    }
}

pub fn run(config:Config) -> Result<(), Box<dyn Error>>{
    let contents = fs::read_to_string(config.file_path)?;

    let results = if config.ingore_case{
        search_case_insensitive(&config.query,&contents)
    } else {
        search(&config.query,&contents)
    };
    for line in results{
        println!("{}",line);
    }
    Ok(())
}

pub fn search<'a>(query:&str, contents: &'a str) -> Vec<&'a str>{
    //contents has a lifetime since the return vector will be referencing its lifetimes, the query string doesn't matter
    contents
        .lines()
        .filter(|line| line.contains(query))
        .collect()
}

pub fn search_case_insensitive<'a>(query:&str, contents: &'a str) -> Vec<&'a str>{
    let mut results = Vec::new();
    for line in contents.lines(){
        if line.to_lowercase().contains(&query.to_lowercase()){
            results.push(line)
        }
    }
    results
}

#[cfg(test)]
mod tests{
    use super::*;

    #[test]
    fn case_sensitive(){
        let query="duct";
        let contents="\
Rust:
safe, fast, productive.
Pick three.
Duct Tape";

        assert_eq!(vec!["safe, fast, productive."],search(query,contents))
    }

    #[test]
    fn case_insensitive(){
        let query = "rUsT";
        let contents = "\
Rust:
safe, fast, productive.
Pick three.
Trust me.";
        assert_eq!(
            vec!["Rust:","Trust me."],
            search_case_insensitive(query,contents)
        )
    }
}

#[derive(PartialEq, Debug)]
struct Shoe{
    size: u32,
    style: String,
}

fn shoes_in_size(shoes:Vec<Shoe>, shoe_size:u32) -> Vec<Shoe>{
    shoes.into_iter().filter(|s| s.size == shoe_size).collect()
}
#[cfg(test)]
mod tests_2{
    use super::*;
    #[test]
    fn filters_by_size(){
        let shoes = vec![
            Shoe{
                size:10,
                style: String::from("sneaker")
            },
            Shoe{
                size:13,
                style: String::from("sandal")
            },
            Shoe{
                size: 10,
                style: String::from("boot")

            }
        ];

        let in_my_size = shoes_in_size(shoes,10);
        assert_eq!(
            in_my_size,
            vec![
                Shoe{
                    size:10,
                    style: String::from("sneaker")
                },
                Shoe{
                    size:10,
                    style: String::from("boot")
                }
            ]
        );
    }
}