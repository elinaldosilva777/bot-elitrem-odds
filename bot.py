import os
import re
from telethon import TelegramClient, events

# 1. Configurações via Secrets do GitHub
# Certifique-se de que cadastrou API_ID, API_HASH, BOT_TOKEN, ID_ORIGEM e ID_DESTINO no GitHub
api_id = int(os.environ.get('API_ID'))
api_hash = os.environ.get('API_HASH')
bot_token = os.environ.get('BOT_TOKEN')
origem_id = int(os.environ.get('ID_ORIGEM'))
destino_id = int(os.environ.get('ID_DESTINO'))

# 2. Inicialização do Cliente
client = TelegramClient('sessao_elitrem', api_id, api_hash).start(bot_token=bot_token)

print("🤖 EliTrem Bot está monitorando as SuperOdds...")

@client.on(events.NewMessage(chats=origem_id))
async def handler(event):
    # Pega o texto da mensagem original
    texto_original = event.raw_text
    if not texto_original:
        return

    # Filtro de Segurança: Só processa se a mensagem parecer uma aposta/odd
    termos_filtro = ['ODD', 'SUPER', 'BILHETE', 'TURBINADA', 'PROMO', 'CASH']
    if any(termo in texto_original.upper() for termo in termos_filtro):
        
        # --- INÍCIO DA TRADUÇÃO ESTILO ELITREM ---
        
        # 1. Substitui os Títulos e Emojis de Identidade
        novo_texto = texto_original.replace("💎 SUPER ODDS", "🚂💨 ELITREM | SUPER ODD")
        novo_texto = novo_texto.replace("⚡️ SUPER ODDS", "🚂💨 ELITREM | SUPER ODD")
        novo_texto = novo_texto.replace("💎", "✅").replace("⚡️", "🔥")
        
        # 2. Adapta Termos Técnicos
        novo_texto = novo_texto.replace("Odd turbinada de", "Cotação subiu:")
        novo_texto = novo_texto.replace("Bilhete disponível no link", "🔥 ENTRADA LIBERADA")
        novo_texto = novo_texto.replace("BILHETE PRONTO", "COPIAR ENTRADA")
        novo_texto = novo_texto.replace("Entrada de perfil", "Sugestão de")
        
        # 3. LIMPEZA DE LINKS (Remove links de afiliados de terceiros)
        # Remove links que começam com http ou
