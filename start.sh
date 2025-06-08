#!/bin/bash

# 建立環境（如果還沒建立過）
conda env create -f environment.yml --force

# 啟用環境
source $(conda info --base)/etc/profile.d/conda.sh
conda activate Graphql