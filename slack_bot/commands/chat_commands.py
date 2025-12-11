import logging

logger = logging.getLogger("ChatCommands")

#Kanala veya kişiye mesaj gönderme
def send_message_func(client, channel_id, text):
    try:
        # channel_id yerine kullanıcı ID'si yazılırsa işlem tamamlanır.
        # Kanal ID'si yazılırsa kanala gider.
        client.chat_postMessage(channel=channel_id, text=text)
        return f"✅ Mesaj gönderildi!"
    except Exception as e:
        logger.error(f"Mesaj hatasi: {e}")
        return f"Mesaj gönderilemedi: {e}"

#Thread 
def send_thread_message_func(client, channel_id, thread_ts, text):
    #thread_ts: Hangi mesaja cevap verileceğinin zaman damgası ID'si.
    try:
        client.chat_postMessage(channel=channel_id, text=text, thread_ts=thread_ts)
        return f"Thread mesaji gönderildi!"
    except Exception as e:
        logger.error(f"Thread hatasi: {e}")
        return f"Thread mesaji gönderilemedi: {e}"