import asyncio
import websockets
import os
import random
from faker import Faker

fake = Faker("pt_BR")
nome = os.getenv("NOME_USUARIO", "Anon")

async def enviar_mensagens():
    while True:
        try:
            async with websockets.connect("ws://websocket-server:8765") as ws:
                print(f"🧑‍🚀 {nome} entrou na sala.")
                while True:
                    texto = fake.paragraph(nb_sentences=2)
                    mensagem = f"{nome}: {texto}"
                    print(f"✉️ Enviando: {mensagem}")
                    await ws.send(mensagem)
                    await asyncio.sleep(random.uniform(1.5, 3))
        except Exception as e:
            print(f"⚠️ Erro: {e}. Tentando reconectar em 5s...")
            await asyncio.sleep(5)

asyncio.run(enviar_mensagens())