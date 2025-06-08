# GraphQL FastAPI Project

本專案是一個使用 FastAPI + GraphQL 的後端應用，使用 Conda 管理環境，並透過 Docker 容器化部署。

---

## 📦 環境建置

### 使用 Docker 建置與啟動

```bash
# 1. 建立 Docker Image
docker build -t graphql -f docker/Dockerfile .

# 2. 啟動容器（暫時性）
docker run -it --rm -p 8000:8000 graphql

# 3.容器啟動後，請於容器內部執行以下指令啟動伺服器：
conda run -n Graphql python /app/start_server.py

# 4.伺服器啟動後，可透過以下網址進入 GraphQL Playground：
http://localhost:8000/graphql
```

### 測試指令

```
pytest test/test_graphql.py
```

### commit更新

```
pytest test/test_graphql.py
```
