#!/bin/bash

#SBATCH -A research
#SBATCH -n 16
#SBATCH --nodes=1
#SBATCH --gpus=4
#SBATCH --mincpus 32
#SBATCH --mem-per-cpu=2048
#SBATCH --partition=long
#SBATCH --time=4-00:00:00

echo "Loading necessary modules"
module load cudnn/7.6.5-cuda-10.2
module load cudnn/8.2.1-cuda-11.3
module load python/3.7.4

export CUDA_VISIBLE_DEVICES=0,1,2,3

echo "Making folder for current job"
cd /scratch
[ -d "aforakhilesh" ] && rm -rf aforakhilesh
mkdir aforakhilesh
chmod 700 aforakhilesh
cd aforakhilesh

echo "Copying the code over"
cp -rip /home2/aforakhilesh/bertology/ ./
cd bertology

echo "Loading python environment"
conda activate research

echo "Installing required python modules"
conda install -c anaconda json
conda install -c anaconda transformers
conda install -c anaconda pandas
conda install -c anaconda numpy
conda install -c pytorch pytorch
conda install -c anaconda scikit-learn

PYTHONPATH=. \
    python3 ada.py

echo "JOB DONE"

cp -rip ./gold/malayalam/indic_concat_mal.txt  /home2/aforakhilesh/
