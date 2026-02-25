from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.responses import HTMLResponse

app = FastAPI()

# Храним подключенные сокеты
clients: set[WebSocket] = set()


@app.get("/")
def home():
    # Мини-страница для теста из браузера
    return HTMLResponse("""
<!doctype html>
<html>
  <head><meta charset="utf-8"><title>WS demo</title></head>
  <body>
    <h3>WebSocket demo</h3>
    <div>
      <input id="msg" placeholder="Type message..." />
      <button onclick="sendMsg()">Send</button>
      <button onclick="ping()">Ping</button>
    </div>
    <pre id="log"></pre>

    <script>
      const log = (s) => document.getElementById('log').textContent += s + "\\n";
      const ws = new WebSocket("ws://localhost:8000/ws");

      ws.onopen = () => log("[open] connected");
      ws.onmessage = (e) => log("[message] " + e.data);
      ws.onclose = () => log("[close] disconnected");
      ws.onerror = (e) => log("[error] " + e);

      function sendMsg() {
        const v = document.getElementById('msg').value;
        ws.send(v);
        document.getElementById('msg').value = "";
      }
      function ping() { ws.send("/ping"); }
    </script>
  </body>
</html>
""")


@app.websocket("/ws")
async def ws_endpoint(ws: WebSocket):
    await ws.accept()
    clients.add(ws)

    # приветствие только этому клиенту
    await ws.send_text("Welcome! Type anything. Use /ping to get pong. Use /who to see online count.")

    # уведомим всех о новом подключении
    await broadcast(f"[system] user joined, online={len(clients)}")

    try:
        while True:
            msg = await ws.receive_text()

            msg = msg.strip()
            if not msg:
                continue

            # простые "команды"
            if msg == "/ping":
                await ws.send_text("pong")
                continue

            if msg == "/who":
                await ws.send_text(f"online={len(clients)}")
                continue

            # обычное сообщение — рассылаем всем
            await broadcast(f"[chat] {msg}")

    except WebSocketDisconnect:
        pass
    finally:
        if ws in clients:
            clients.remove(ws)
        await broadcast(f"[system] user left, online={len(clients)}")


async def broadcast(text: str):
    dead = []
    for c in clients:
        try:
            await c.send_text(text)
        except Exception:
            dead.append(c)

    # чистим отвалившихся
    for d in dead:
        clients.discard(d)

