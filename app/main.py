from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from ariadne import make_executable_schema, gql
from ariadne.asgi import GraphQL

# 匯入 Query/Mutation Resolver
from .resolvers import query, mutation  # 假設你有 app/resolvers.py

# 讀取 schema.graphql
with open("app/schema.graphql", "r") as f:
    type_defs = gql(f.read())

# 建立 Ariadne schema
schema = make_executable_schema(type_defs, query, mutation)

# 建立 FastAPI 應用
app = FastAPI()

# 加入 CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 或 ["https://yourfrontend.com"]
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 掛載 /graphql endpoint
app.mount("/graphql", GraphQL(schema, debug=True))
