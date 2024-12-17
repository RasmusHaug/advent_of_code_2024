use std::fs::File;
use std::io::{self, BufRead};

fn main() -> Result<(), Box<dyn std::error::Error>> {
    let path: &str = "input.txt";
    let file: File = File::open(path)?;
    let reader: io::BufReader<File> = io::BufReader::new(file);

    let mut left_list = Vec::new();
    let mut right_list = Vec::new();

    for line in reader.lines() {
        let line = line?;
        let numbers: Vec<i32> = line
            .split_whitespace()
            .filter_map(|s| s.parse().ok())
            .collect();

        if numbers.len() == 2 {
            // Push numbers to corresponding list.
            left_list.push(numbers[0]);
            right_list.push(numbers[1]);
        }
    }

    println!("LeftList: {left_list}\n");
    println!("RightList: {right_list}")
}

fn solution_1() {}

fn solution_2() {}
