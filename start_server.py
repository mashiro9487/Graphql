import asyncio
import threading
import webbrowser

import uvicorn

from app.init_db import init  # 匯入初始化函式


def open_browser():
    webbrowser.open("http://172.20.10.2:8000/graphql")


async def main():
    await init()  # 初始化資料庫
    config = uvicorn.Config("app.main:app", host="0.0.0.0", port=8000, reload=True)
    server = uvicorn.Server(config)
    threading.Timer(1.5, open_browser).start()
    await server.serve()


if __name__ == "__main__":
    asyncio.run(main())
