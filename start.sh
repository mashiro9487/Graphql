#!/bin/bash

ENV_NAME="Graphql"

if conda env list | grep -q "^$ENV_NAME\s"; then
    echo "Environment $ENV_NAME already exists. Skipping creation."
else
    echo "Creating environment $ENV_NAME..."
    conda env create -f environment.yml
fi

source $(conda info --base)/etc/profile.d/conda.sh
conda activate $ENV_NAME

# 你想跑的命令，像是啟動伺服器
# python app/main.py

