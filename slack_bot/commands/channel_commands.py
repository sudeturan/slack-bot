import logging

# Log kayıtçısını al
logger = logging.getLogger("ChannelCommands")

#Yeni kanal oluşturma
def create_channel_func(client, channel_name):
    try:
        # Slack API'sine kanal açma isteği gönderme yapısı
        response = client.conversations_create(name=channel_name)
        
        # Oluşturulan kanalın ID'sini aldıktan sonra
        channel_id = response["channel"]["id"]
        logger.info(f"Kanal olusturuldu: {channel_name} (ID: {channel_id})")
        return f"'{channel_name}' isimli kanal basariyla olusturuldu! ID: {channel_id}"

    except Exception as e:
        logger.error(f"Kanal olusturma hatasi: {e}")
        return f"Kanal olusturulamadi. Hata: {e}"

#Var olan kanali arşivleme
def archive_channel_func(client, channel_id):
    try:
        client.conversations_archive(channel=channel_id)
        logger.info(f"Kanal arsivlendi: {channel_id}")
        return f"Kanal ({channel_id}) basariyla arsivlendi (silindi)."
    except Exception as e:
        logger.error(f"Arsivleme hatasi: {e}")
        return f"Kanal arsivlenemedi. Hata: {e}"