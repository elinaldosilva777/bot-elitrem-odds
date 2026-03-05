import os
import re
import asyncio
from telethon import TelegramClient, events
from telethon.sessions import StringSession

# Dados que você já tem nos Secrets
api_id = int(os.environ.get('API_ID'))
api_hash = os.environ.get('API_HASH')
session_str = os.environ.get('TELEGRAM_SESSION')
origem_id = int(os.environ.get('ID_ORIGEM'))
destino_id = int(os.environ.get('ID_DESTINO'))

# Inicia o cliente usando a String Session (sem arquivos!)
client = TelegramClient(StringSession(session_str), api_id, api_hash)

async def main():
    print("🚂 EliTrem Tips: Iniciando motor via String...")
    await client.connect()
    
    # Verifica se a string funcionou
    if not await client.is_user_authorized():
        print("❌ ERRO: A String Session expirou ou é inválida.")
        return

    print("✅ CONECTADO! O Trem do Green está nos trilhos.")

    @client.on(events.NewMessage(chats=origem_id))
    async def handler(event):
        # Filtro de palavras-chave para o EliTrem Tips
        if event.raw_text and any(p in event.raw_text.upper() for p in ['ODD', 'SUPER', 'BILHETE']):
            # Limpa links e formata a mensagem
            texto = re.sub(r'https?://\S+', '', event.raw_text)
            final = f"🚂💨 **ELITREM TIPS**\n\n{texto.strip()}\n\n🚀 @EliTremTips"
            
            try:
                await client.send_message(destino_id, final, file=event.media)
                print("🎯 Dica enviada para o grupo!")
            except Exception as e:
                print(f"❌ Erro ao enviar: {e}")

    await client.run_until_disconnected()

if __name__ == '__main__':
    # Roda o bot de forma compatível com o Python do GitHub
    asyncio.run(main())
