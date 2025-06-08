from ariadne import make_executable_schema, gql
from ariadne.asgi import GraphQL
from fastapi import FastAPI

from .resolvers import query, mutation

# 讀取 GraphQL schema
with open("app/schema.graphql", "r") as f:
    type_defs = gql(f.read())

# 組合 schema
schema = make_executable_schema(type_defs, query, mutation)
print("GraphQL schema loaded successfully.")

# 啟用 FastAPI 應用
app = FastAPI()
app.mount("/graphql", GraphQL(schema, debug=True))
