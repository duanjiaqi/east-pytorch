#!/bin/bash
srun --partition=SenseMediaA --mpi=pmi2 --gres=gpu:1 -n1 --ntasks-per-node=1 --job-name=eval /mnt/lustre/duanjiaqi/anaconda3/envs/dist/bin/python scale_eval.py
