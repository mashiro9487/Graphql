from ariadne import QueryType, MutationType
from passlib.context import CryptContext
from sqlalchemy.future import select

from app.db import async_session
from app.models import User

# 建立密碼雜湊上下文，使用 bcrypt
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

query = QueryType()
mutation = MutationType()


@query.field("hello")
def resolve_hello(_, info):
    return "Hello from GraphQL!"


@mutation.field("login")
async def resolve_login(_, info, email, password):
    async with async_session() as session:
        result = await session.execute(select(User).where(User.email == email))
        user = result.scalar_one_or_none()
        if not user:
            return "Invalid credentials."

        # 驗證密碼
        if not pwd_context.verify(password, user.password):
            return "Invalid credentials."

        return "Login successful!"


@mutation.field("register")
async def resolve_register(_, info, email, password):
    async with async_session() as session:
        # 檢查是否已存在
        result = await session.execute(select(User).where(User.email == email))
        user = result.scalar_one_or_none()
        if user:
            return {"success": False, "message": "Email already registered"}

        # 密碼雜湊
        hashed_password = pwd_context.hash(password)

        # 新增使用者
        new_user = User(email=email, password=hashed_password)
        session.add(new_user)
        await session.commit()

        return {"success": True, "message": "Register successful!"}
