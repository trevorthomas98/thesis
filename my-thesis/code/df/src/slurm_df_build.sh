#!/bin/bash
#SBATCH --job-name=pickle_thomas_out
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --time=10-00:00:00
                                                           
#SBATCH -o /home/trevor.thomas/thesis/new/my-thesis/runs/df_build.%j.out
#SBATCH --partition=monaco
#SBATCH --mem=32G
#SBATCH --gres=gpu:1
#SBATCH --mail-type=END              
#SBATCH --mail-user=trevor.thomas@nps.edu
 
#. /etc/profile
#/share/spack/gcc-7.2.0/miniconda3-4.5.12-gkh/condabin/conda activate tf-2.6
 

#python3 /home/paul.duhe/thesis/new/small_thesis_project/code/df_script.py
python3 /home/trevor.thomas/thesis/my-thesis/code/get_shortest.py




