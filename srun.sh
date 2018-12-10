#!/bin/bash
srun -w SH-IDC1-10-5-34-180 --partition=SenseMediaA --mpi=pmi2 --gres=gpu:2 -n1 --ntasks-per-node=1 --job-name=org-nm /mnt/lustre/duanjiaqi/anaconda3/envs/dist/bin/python main.py
