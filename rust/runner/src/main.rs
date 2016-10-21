#![cfg_attr(not(feature = "with-syntex"), feature(proc_macro, plugin))]
#[cfg(not(feature = "with-syntex"))]
use std::env;

extern crate time;
use time::PreciseTime;

#[macro_use]
extern crate serde_derive;

extern crate serde;
extern crate serde_json;

use std::fs::File;
use std::io::{Read, Write};

#[derive(Debug, PartialEq, Serialize, Deserialize)]
struct DataElement {
    ident: String,
    attribute_1: String,
    attribute_2: String,
    attribute_3: String,
}

#[derive(Debug, PartialEq, Serialize, Deserialize)]
struct Data {
    data: Vec<DataElement>
}

fn main() {
    // handle command line arguments
    let args: Vec<_> = env::args().collect();
    if args.len() != 3 {
        println!("Usage: test_rust <input> <output>");
        std::process::exit(1);
    }

    // read and parse input
    let read_start = PreciseTime::now();
    let mut input_file = File::open(&env::args().nth(1).unwrap()).unwrap();
    let mut input_text = String::new();
    input_file.read_to_string(&mut input_text).unwrap();
    let parse_start = PreciseTime::now();
    let input_data: Data = serde_json::from_str(&input_text).unwrap();
    let parse_end = PreciseTime::now();
    let read_end = PreciseTime::now();

    // serialize and write output
    let write_start = PreciseTime::now();
    let serialize_start = PreciseTime::now();
    let output_text = serde_json::to_string(&input_data).unwrap();
    let serialize_end = PreciseTime::now();
    let mut output_file = File::create(&env::args().nth(2).unwrap()).unwrap();
    output_file.write_all(output_text.as_bytes()).unwrap();
    let write_end = PreciseTime::now();

    // stats
    println!("r:{}", read_start.to(read_end));
    println!("p:{}", parse_start.to(parse_end));
    println!("w:{}", write_start.to(write_end));
    println!("s:{}", serialize_start.to(serialize_end));
}
