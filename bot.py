import os
import re
from telethon import TelegramClient, events

api_id = int(os.environ.get('API_ID'))
api_hash = os.environ.get('API_HASH')
origem_id = int(os.environ.get('ID_ORIGEM'))
destino_id = int(os.environ.get('ID_DESTINO'))

# Certifique-se que o nome aqui é IGUAL ao arquivo que você subiu
client = TelegramClient('sessao_user.session', api_id, api_hash)

print("🚂 EliTrem UserBot tentando conectar...")

@client.on(events.NewMessage(chats=origem_id))
async def handler(event):
    if not event.raw_text: return
    if any(p in event.raw_text.upper() for p in ['ODD', 'SUPER', 'BILHETE']):
        texto = re.sub(r'https?://\S+', '', event.raw_text)
        final = "🚂💨 **ELITREM TIPS**\n\n" + texto.strip() + "\n\n🚀 @EliTremTips"
        await client.send_message(destino_id, final, file=event.media)

# O comando start() sem parâmetros evita que ele peça o telefone no GitHub
async def main():
    await client.start()
    print("✅ EliTrem conectado com sucesso e monitorando!")
    await client.run_until_disconnected()

import asyncio
if __name__ == '__main__':
    asyncio.run(main())
