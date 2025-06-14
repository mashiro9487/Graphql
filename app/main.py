from fastapi import FastAPI
from ariadne.asgi import GraphQL
from ariadne import QueryType, gql, make_executable_schema
from fastapi.middleware.cors import CORSMiddleware

# CORS 設定
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# GraphQL schema
type_defs = gql("""
    type Query {
        hello: String!
    }
""")

query = QueryType()

@query.field("hello")
def resolve_hello(_, info):
    return "Hello from GraphQL!"

schema = make_executable_schema(type_defs, query)

# 掛載 GraphQL 到 /graphql 路徑
app.mount("/graphql", GraphQL(schema, debug=True))
