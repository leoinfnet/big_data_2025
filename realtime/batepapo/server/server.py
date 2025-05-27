import asyncio
import websockets

clientes = set()

async def handler(websocket):
    print("🧑‍💻 Novo usuário conectado.")
    clientes.add(websocket)
    try:
        async for message in websocket:
            print(f"📩 Mensagem recebida: {message}")
            await asyncio.gather(*[c.send(message) for c in clientes if c != websocket])
    except websockets.ConnectionClosed:
        print("❌ Conexão encerrada.")
    finally:
        clientes.remove(websocket)

async def main():
    print("🟢 Servidor WebSocket escutando em ws://0.0.0.0:8765")
    async with websockets.serve(handler, "0.0.0.0", 8765):
        await asyncio.Future()

asyncio.run(main())
