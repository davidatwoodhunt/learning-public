fn main(){
    let needle = 42;

    let haystack = vec![1,2,3,4,5,42,132,429,1420,111111];

    for item in &haystack{
        let result = match item {
            42 | 132 => "Hit!",
            _ => "Miss",
        };
        if result == "Hit!"{
            println!("{}: {}",item,result);
        }
    }

}