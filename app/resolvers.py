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


# 新增 register mutation
@mutation.field("register")
def resolve_register(_, info, email, password):
    # 這裡你可以加入註冊邏輯，例如寫進資料庫
    print(f"Registering user: {email}")
    # 假設註冊成功回傳訊息
    return "Register successful!"
