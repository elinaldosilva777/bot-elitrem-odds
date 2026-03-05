import os
import re
import asyncio
from telethon import TelegramClient, events

# Puxa as variáveis das Secrets
api_id = int(os.environ.get('API_ID'))
api_hash = os.environ.get('API_HASH')
origem_id = int(os.environ.get('ID_ORIGEM'))
destino_id = int(os.environ.get('ID_DESTINO'))

# IMPORTANTE: O nome aqui deve ser EXATAMENTE o nome do arquivo que você subiu
# Se o arquivo no GitHub se chama 'sessao_user', mude para 'sessao_user' aqui.
client = TelegramClient('sessao_user.session', api_id, api_hash)

async def main():
    print("🔄 Tentando conectar ao Telegram...")
    await client.connect()
    
    if not await client.is_user_authorized():
        print("❌ ERRO: O arquivo de sessão não foi reconhecido ou expirou.")
        return

    print("✅ EliTrem Conectado! Monitorando mensagens...")

    @client.on(events.NewMessage(chats=origem_id))
    async def handler(event):
        if event.raw_text and any(p in event.raw_text.upper() for p in ['ODD', 'SUPER', 'BILHETE']):
            texto = re.sub(r'https?://\S+', '', event.raw_text)
            final = f"🚂💨 **ELITREM TIPS**\n\n{texto.strip()}\n\n🚀 @EliTremTips"
            await client.send_message(destino_id, final, file=event.media)
            print("🚀 Tip enviada para o grupo!")

    await client.run_until_disconnected()

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
