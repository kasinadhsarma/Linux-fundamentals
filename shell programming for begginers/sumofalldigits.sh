#!/bin/bash

echo "Enter numbers"
read nums

while [ $nums -gt 0 ]; do
    mod=$((nums % 10))
    sum=$((sum + mod ))
    nums=$((nums / 10 ))
done

echo "SUM is " $sum
