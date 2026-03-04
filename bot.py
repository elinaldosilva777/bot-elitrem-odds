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
    texto_original = event.raw_text
    # ESTA LINHA VAI MOSTRAR TUDO NO LOG DO GITHUB
    print(f"📥 Mensagem recebida da origem: {texto_original[:50]}...") 

    if not texto_original:
        return

    # Filtro mais sensível (aceita minúsculas e maiúsculas)
    termos = ['ODD', 'SUPER', 'BILHETE', 'TURBINADA', 'BETANO', 'BET365', 'GREEN']
    if any(termo in texto_original.upper() for termo in termos):
        print("🎯 Filtro aprovado! Tentando enviar para o EliTrem Tips...")
        
        # --- PERSONALIZAÇÃO ---
        novo_texto = texto_original.replace("💎 SUPER ODDS", "            ELITREM | SUPER ODD")
        novo_texto = re.sub(r'https?://\S+', '', novo_texto)
        assinatura = "\n\n🚀 **Siga o Trem do Green:** @EliTremTips"
        texto_final = novo_texto.strip() + assinatura
        
        try:
            await client.send_message(destino_id, texto_final, file=event.media)
            print("✅ SUCESSO: Mensagem enviada para o seu grupo!")
        except Exception as e:
            # SE DER ERRO DE PERMISSÃO OU ID, VAI APARECER AQUI:
            print(f"❌ ERRO AO ENVIAR: {e}")
    else:
        print("⏩ Mensagem ignorada pelo filtro (não continha as palavras-chave).")
        
        # 3. LIMPEZA DE LINKS (Remove links de afiliados de terceiros)
        # Remove links que começam com http ou
