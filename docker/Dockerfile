FROM continuumio/miniconda3

WORKDIR /app

# 複製環境設定
COPY ../env/environment.yml ./environment.yml

# 建立 conda 環境
RUN conda env create -f environment.yml

# 複製 app 原始碼 (記得相對路徑從 docker/ 目錄算起)
COPY ../app ./app

# 把 start_server.py 也複製進來（如果你用它來啟動服務）
COPY ../start_server.py ./start_server.py

# 這裡用你的 conda 環境名稱 Graphql，並啟動 uvicorn
# CMD ["conda", "run", "-n", "Graphql", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
