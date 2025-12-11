import os
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
from slack_bot.core.config import SLACK_BOT_TOKEN, SLACK_APP_TOKEN
from slack_bot.core.logger import get_logger

# Fonksiyonları Aktarma
from slack_bot.commands.channel_commands import create_channel_func, archive_channel_func
from slack_bot.commands.user_commands import (
    get_id_by_email_func, get_email_by_id_func,
    invite_users_by_id_list, invite_users_by_email_list,
    kick_users_by_id_list, kick_users_by_email_list
)
from slack_bot.commands.chat_commands import send_message_func, send_thread_message_func

logger = get_logger("BotClient")
app = App(token=SLACK_BOT_TOKEN)

#Kanal açma
@app.message("kanal aç")
def handle_create(message, say, client):
    parts = message.get("text").split()
    if len(parts) >= 3:
        say(create_channel_func(client, parts[2]))

#Kanal silme
@app.message("kanal sil")
def handle_archive(message, say, client):
    # NOT: Botlar kanalı tamamen silemez, ARŞİVLER.
    parts = message.get("text").split()
    if len(parts) >= 3:
        say(archive_channel_func(client, parts[2]))
    else:
        say("⚠️ Örnek: kanal sil C12345")

#Kanal arşivleme
@app.message("kanal arşivle") # Alternatif komut
def handle_archive_alt(message, say, client):
    parts = message.get("text").split()
    if len(parts) >= 3:
        say(archive_channel_func(client, parts[2]))

#İstenen bilgiyi bulma - id
@app.message("id bul")
def handle_id_find(message, say, client):
    text = message.get("text")
    if "<mailto:" in text:
        email = text.split("|")[1].replace(">", "")
    else:
        parts = text.split()
        email = parts[2] if len(parts) >= 3 else None
        
    if email:
        uid = get_id_by_email_func(client, email)
        say(f"Kullanici ID: `{uid}`") if uid else say("Bulunamadi.")
    else:
        say("Örnek: id bul a@b.com")

#İstenen bilgiyi bulma - email
@app.message("email bul")
def handle_email_find(message, say, client):
    parts = message.get("text").split()
    if len(parts) >= 3:
        email = get_email_by_id_func(client, parts[2].upper())
        say(f"E-posta: {email}") if email else say("Bulunamadi.")

#Kanala ekleme - id
@app.message("davet et id")
def handle_invite_ids(message, say, client):
    # Komut: davet et id U1,U2,U3 C_KANAL
    parts = message.get("text").split()
    if len(parts) >= 5:
        id_list = parts[3].split(",") # Virgülle ayır
        channel_id = parts[4]
        say(f"🔄 {len(id_list)} kişi ID ile ekleniyor...")
        say(invite_users_by_id_list(client, channel_id, id_list))
    else:
        say("⚠️ Örnek: davet et id U123,U456 C_KANAL_ID")

#Kanala ekleme - email
@app.message("davet et email")
def handle_invite_emails(message, say, client):
    # Komut: davet et email a@b.com,x@y.com C_KANAL
    text = message.get("text")
    parts = text.split()
    if len(parts) >= 5:
        # Link temizleme mantığı biraz karmaşık olabilir, basit tutalım:
        raw_emails = parts[3]
        # Slack format temizliği (<mailto:a@b.com|a@b.com> -> a@b.com)
        clean_emails = []
        for item in raw_emails.split(","):
            if "|" in item: item = item.split("|")[1].replace(">", "")
            clean_emails.append(item)
            
        channel_id = parts[4]
        say(f"🔄 {len(clean_emails)} e-posta taranıyor ve ekleniyor...")
        say(invite_users_by_email_list(client, channel_id, clean_emails))
    else:
        say("⚠️ Örnek: davet et email a@b.com,c@d.com C_KANAL_ID")

#Kanaldan çıkarma - id 
@app.message("çıkar id")
def handle_kick_ids(message, say, client):
    parts = message.get("text").split()
    if len(parts) >= 4:
        id_list = parts[2].split(",")
        channel_id = parts[3]
        say(kick_users_by_id_list(client, channel_id, id_list))
    else:
        say("⚠️ Örnek: çıkar id U123,U456 C_KANAL_ID")

#Kanaldan çıkarma - email
@app.message("çıkar email")
def handle_kick_emails(message, say, client):
    text = message.get("text")
    parts = text.split()
    if len(parts) >= 4:
        raw_emails = parts[2]
        clean_emails = []
        for item in raw_emails.split(","):
            if "|" in item: item = item.split("|")[1].replace(">", "")
            clean_emails.append(item)
            
        channel_id = parts[3]
        say(f"🔄 E-postalar bulunup çıkarılıyor...")
        say(kick_users_by_email_list(client, channel_id, clean_emails))
    else:
        say("⚠️ Örnek: çıkar email a@b.com,c@d.com C_KANAL_ID")

#Mesaj gönderme
@app.message("mesaj gönder")
def handle_msg(message, say, client):
    text = message.get("text")
    parts = text.split(" ", 3)
    if len(parts) >= 4:
        say(send_message_func(client, parts[2], parts[3]))

#Thread
@app.message("thread")
def handle_thread(message, say, client):
    # Mesajın kendisine thread açar
    send_thread_message_func(client, message["channel"], message["ts"], "🧵 Thread testi başarılı!")

if __name__ == "__main__":
    SocketModeHandler(app, SLACK_APP_TOKEN).start()
