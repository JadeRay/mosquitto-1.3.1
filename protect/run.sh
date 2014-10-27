#!/bin/bash

echo "Starting to run mosqutto pressure testing..."

n=30
arg=2

if [ $# -ne 1 ]
then
    echo "Arguments should be exactly 1!"
    echo "Choose your routine!"
    exit 1
fi

run=$1
now=$0

while [ $n != 0 ]
do
    ./$run -h $arg &
    sleep 10
    for pid in $(ps -ef|grep "$run"|grep -v "grep"|grep -v "$now"|awk '{print $2}')
    do
        kill -9 $pid
    done
    arg=$(($arg + 2))
    n=$(($n - 1))
done

echo "Testing Done!"
