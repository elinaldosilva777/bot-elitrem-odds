import os
import re
import asyncio
from telethon import TelegramClient, events
from telethon.sessions import StringSession

# Puxa tudo que você configurou nos Secrets do GitHub
api_id = int(os.environ.get('API_ID'))
api_hash = os.environ.get('API_HASH')
session_str = os.environ.get('TELEGRAM_SESSION') # O código gigante
origem_id = int(os.environ.get('ID_ORIGEM'))
destino_id = int(os.environ.get('ID_DESTINO'))

# Inicia o motor do EliTrem sem precisar de arquivos .session
client = TelegramClient(StringSession(session_str), api_id, api_hash)

async def main():
    print("🚂 EliTrem Tips: Iniciando motor via String...")
    await client.connect()
    
    if not await client.is_user_authorized():
        print("❌ ERRO: A String Session é inválida ou expirou.")
        return

    print("✅ CONECTADO! O Trem do Green está online.")

    @client.on(events.NewMessage(chats=origem_id))
    async def handler(event):
        if event.raw_text and any(p in event.raw_text.upper() for p in ['ODD', 'SUPER', 'BILHETE']):
            texto = re.sub(r'https?://\S+', '', event.raw_text)
            final = f"🚂💨 **ELITREM TIPS**\n\n{texto.strip()}\n\n🚀 @EliTremTips"
            await client.send_message(destino_id, final, file=event.media)
            print("🎯 Tip enviada com sucesso!")

    await client.run_until_disconnected()

if __name__ == '__main__':
    asyncio.run(main())
