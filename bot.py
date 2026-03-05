import os
import re
from telethon import TelegramClient, events

# Puxa os dados das Secrets que você já configurou
api_id = int(os.environ.get('API_ID'))
api_hash = os.environ.get('API_HASH')
origem_id = int(os.environ.get('ID_ORIGEM'))
destino_id = int(os.environ.get('ID_DESTINO'))

# Inicia a conexão usando o arquivo que você subiu
client = TelegramClient('sessao_user', api_id, api_hash)

print("🚂 EliTrem UserBot Ativo e Monitorando!")

@client.on(events.NewMessage(chats=origem_id))
async def handler(event):
    if not event.raw_text: return
    
    # Filtro de palavras-chave para as SuperOdds
    if any(p in event.raw_text.upper() for p in ['ODDS', 'SUPER', 'BILHETE', 'BET']):
        # Limpa os links originais
        texto = re.sub(r'https?://\S+', '', event.raw_text)
        # Formatação com a marca do EliTrem Tips
        final = "🚂💨 **ELITREM TIPS**\n\n" + texto.strip() + "\n\n🚀 @EliTremTips"
        
        # Envia para o seu grupo de destino (o privado)
        await client.send_message(destino_id, final, file=event.media)

client.start()
client.run_until_disconnected()
