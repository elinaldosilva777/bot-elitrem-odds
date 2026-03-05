import os
import re
import asyncio
from telethon import TelegramClient, events

# Puxa as Secrets configuradas no GitHub
api_id = int(os.environ.get('API_ID'))
api_hash = os.environ.get('API_HASH')
origem_id = int(os.environ.get('ID_ORIGEM'))
destino_id = int(os.environ.get('ID_DESTINO'))

# NOME EXATO DO ARQUIVO QUE VOCÊ SUBIU
nome_sessao = 'sessao_user.session' 

client = TelegramClient(nome_sessao, api_id, api_hash)

async def main():
    print("🚀 EliTrem Tips: Iniciando conexão segura...")
    
    # Tenta conectar sem pedir dados novos ao servidor
    await client.connect()
    
    # Verifica se a sua "chave" de sessão é válida
    if not await client.is_user_authorized():
        print("❌ ERRO: O arquivo de sessão não foi reconhecido.")
        print("Dica: Tente gerar o arquivo novamente no seu PC se este erro persistir.")
        return

    print("✅ SUCESSO! O EliTrem está online e monitorando o grupo.")

    @client.on(events.NewMessage(chats=origem_id))
    async def handler(event):
        if event.raw_text and any(p in event.raw_text.upper() for p in ['ODD', 'SUPER', 'BILHETE']):
            # Remove links para deixar as dicas limpas
            texto = re.sub(r'https?://\S+', '', event.raw_text)
            final = f"🚂💨 **ELITREM TIPS**\n\n{texto.strip()}\n\n🚀 @EliTremTips"
            
            try:
                await client.send_message(destino_id, final, file=event.media)
                print("🎯 Dica encaminhada com sucesso!")
            except Exception as e:
                print(f"❌ Erro ao enviar: {e}")

    await client.run_until_disconnected()

if __name__ == '__main__':
    asyncio.run(main())
