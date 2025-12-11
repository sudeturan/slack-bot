import os
from dotenv import load_dotenv

#.env dosyasındaki verileri yükle
load_dotenv()

#Değişkenleri al ve dışarıya sun
SLACK_BOT_TOKEN = os.getenv("SLACK_BOT_TOKEN")
SLACK_APP_TOKEN = os.getenv("SLACK_APP_TOKEN")

#Eğer tokenler okunamazsa programı durdur ve hata ver
if not SLACK_BOT_TOKEN or not SLACK_APP_TOKEN:
    raise ValueError("HATA: .env dosyasinda SLACK_BOT_TOKEN veya SLACK_APP_TOKEN eksik!")
