#!/usr/bin/env bash

cmd="../circuit_analyse/plot_circuit_files.py"

for file in *.log
do
    cmd=$cmd" "$file
done

exec $cmd
