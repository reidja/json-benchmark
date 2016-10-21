#!/bin/bash

for number in $(seq 1 50)
do
	make run &>> results.txt
done
