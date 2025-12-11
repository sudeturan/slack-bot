try:
    # Yazdığımız modülleri çağırmayı deniyoruz
    from slack_bot.core.config import SLACK_BOT_TOKEN, SLACK_APP_TOKEN
    from slack_bot.core.logger import get_logger

    # Log sistemini test et
    logger = get_logger("Test")
    logger.info("Test basliyor...")

    # Tokenleri kontrol et (Sadece ilk 4 harfini gösterir, güvenlidir)
    if SLACK_BOT_TOKEN and SLACK_APP_TOKEN:
        print(f"✅ Bot Token Okundu: {SLACK_BOT_TOKEN[:4]}...")
        print(f"✅ App Token Okundu: {SLACK_APP_TOKEN[:4]}...")
        logger.info("Sistem harika çalisiyor!")
    else:
        logger.error("❌ Tokenler boş geldi!")

except ImportError as e:
    print("❌ HATA: Dosya yapisi7u6ynda veya kütüphanelerde sorun var.")
    print(f"Detay: {e}")
except Exception as e:
    print(f"❌ Beklenmedik bir hata: {e}")