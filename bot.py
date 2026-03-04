from telethon import TelegramClient, events
import os

# Pega as chaves de forma segura que vamos configurar no próximo passo
api_id = int(os.environ.get('API_ID'))
api_hash = os.environ.get('API_HASH')
bot_token = os.environ.get('BOT_TOKEN')
origem_id = -100XXXXXXXXXX # Vamos trocar pelo ID do canal que você quer copiar
destino_id = -100YYYYYYYYYY # ID do seu grupo EliTrem Tips

# Usando Session em memória para não gerar arquivos no GitHub
client = TelegramClient('sessao_elitrem', api_id, api_hash).start(bot_token=bot_token)

@client.on(events.NewMessage(chats=origem_id))
async def handler(event):
    # Filtro para pegar apenas o que interessa
    termos = ['SuperOdds', 'Odd', 'Promocional', 'Betano', 'Bet365']
    if any(word.lower() in event.raw_text.lower() for word in termos):
        await client.send_message(destino_id, event.message)
        print("✅ Mensagem enviada!")

print("🤖 EliTrem Bot está monitorando...")
client.run_until_disconnected()
