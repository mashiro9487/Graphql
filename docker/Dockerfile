FROM continuumio/miniconda3

WORKDIR /app

# 複製 env 檔與 app 程式碼
COPY env/environment.yml ./environment.yml
COPY app ./app

# 建立 conda 環境（用 python=3.11 避免 asyncpg 錯誤）
RUN conda env create -f environment.yml

# 讓 conda 環境生效 + 安裝 uvicorn
SHELL ["conda", "run", "--no-capture-output", "-n", "Graphql", "/bin/bash", "-c"]

# EXPOSE port
EXPOSE 8000

# 啟動 FastAPI App（透過 conda 執行）
CMD ["conda", "run", "--no-capture-output", "-n", "Graphql", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
