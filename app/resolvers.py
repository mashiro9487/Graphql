from ariadne import QueryType, MutationType

query = QueryType()
mutation = MutationType()

@query.field("hello")
def resolve_hello(_, info):
    return "Hello from GraphQL!"

@mutation.field("login")
def resolve_login(_, info, email, password):
    if email == "test@example.com" and password == "1234":
        return "Login successful!"
    return "Invalid credentials."
