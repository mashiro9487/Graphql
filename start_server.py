import threading
import webbrowser

import uvicorn


def open_browser():
    # 使用你本機在區網的 IP，例如 172.20.10.7
    webbrowser.open("http://172.20.10.7:8000/graphql")

if __name__ == "__main__":
    threading.Timer(1.5, open_browser).start()
    uvicorn.run(
        "app.main:app",
        host="0.0.0.0",  # 🔥 改成監聽所有 IP
        port=8000,
        reload=True
    )
