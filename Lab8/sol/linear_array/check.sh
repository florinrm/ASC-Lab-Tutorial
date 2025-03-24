#!/bin/bash

echo -e "Building..."
make > /dev/null

echo -e "\nTask 1 - constants elimination"
./eliminate_constants

echo -e "\nTask 2 - Loop reorder"
echo -e "\ni-k-j"
./i-k-j 
echo -e "\nj-i-k"
./j-i-k 
echo -e "\nj-k-i"
./j-k-i 
echo -e "\nk-i-j"
./k-i-j 
echo -e "\nk-j-i"
./k-j-i

echo -e "\nTask 3 - Blocked multiplication"
./blocked_matrix_multiplication

echo -e "\nCleaning..."
make clean > /dev/null