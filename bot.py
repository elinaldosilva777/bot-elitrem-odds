import os
import re
import asyncio
from telethon import TelegramClient, events

# Puxa os dados das Secrets
api_id = int(os.environ.get('API_ID'))
api_hash = os.environ.get('API_HASH')
origem_id = int(os.environ.get('ID_ORIGEM'))
destino_id = int(os.environ.get('ID_DESTINO'))

# O nome deve ser exatamente igual ao arquivo que você subiu
nome_sessao = 'sessao_user.session' 

client = TelegramClient(nome_sessao, api_id, api_hash)

async def main():
    print("🚀 EliTrem Tips: Conectando...")
    
    # O connect() não pede telefone, ele apenas usa o arquivo .session
    await client.connect()
    
    if not await client.is_user_authorized():
        print("❌ ERRO: O arquivo .session não foi reconhecido pelo GitHub.")
        return

    print("✅ CONECTADO! O Trem do Green está online.")

    @client.on(events.NewMessage(chats=origem_id))
    async def handler(event):
        if event.raw_text and any(p in event.raw_text.upper() for p in ['ODD', 'SUPER', 'BILHETE']):
            texto = re.sub(r'https?://\S+', '', event.raw_text)
            final = f"🚂💨 **ELITREM TIPS**\n\n{texto.strip()}\n\n🚀 @EliTremTips"
            await client.send_message(destino_id, final, file=event.media)

    await client.run_until_disconnected()

if __name__ == '__main__':
    asyncio.run(main())
