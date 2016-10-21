# Requirements

 * Python 2.7
 * Bash
 * Rust / Cargo
 * C++ Compiler
 * Make

# Results


| Language | Parse (ms) | Serialize (ms) | Memory (KB) | CPU (ms) |
|----------|------------|----------------|-------------|----------|
python-5MB | 0.02619944572 |  0.02141340733  |  74058  | 0.0512
cpp-5MB  |0.01448028 |  0.0108063  |  10292  |  0.0188
rust-5MB   |  0.00858129198  | 0.0042730458   |  24630  |  0.0092
python-75MB  |0.3812372923  |   0.3149325418   |  975096  | 0.6818
cpp-75MB    | 0.21558058  | 0.16391432  | 119515  | 0.3232
rust-75MB  |  0.1310306742   |  0.06301646642  |  254069  | 0.2138

![pic](https://docs.google.com/spreadsheets/d/13EIQpaq-x7vMHDzHCbB0du7ExjsVtY0NswnZLgIUmMk/pubchart?oid=142190828&format=image)
![pic](https://docs.google.com/spreadsheets/d/13EIQpaq-x7vMHDzHCbB0du7ExjsVtY0NswnZLgIUmMk/pubchart?oid=648454899&format=image)
# Usage


```
make clean
make run
make c_runner
make rust_runner
make results
cat results.txt
cat detailed.csv
cat results.csv
```
