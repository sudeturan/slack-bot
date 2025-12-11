# import smtplib
# from email.mime.text import MIMEText
# from email.mime.multipart import MIMEMultipart

# # --- AYARLAR ---
# GMAIL_USER = "senin.mailin@gmail.com"      # Gönderen Mail
# GMAIL_PASSWORD = "xxxx xxxx xxxx xxxx"     # Gmail Uygulama Şifresi (Normal şifre değil!)
# SLACK_INVITE_LINK = "https://join.slack.com/t/......(kopyaladigin-link)......"

# # Davet edilecekler listesi
# davet_listesi = [
#     "arkadas1@gmail.com",
#     "arkadas2@ornek.com",
#     "yeni.uye@sirket.com"
# ]

# def davetiye_gonder(gidecek_adres):
#     try:
#         msg = MIMEMultipart()
#         msg['From'] = GMAIL_USER
#         msg['To'] = gidecek_adres
#         msg['Subject'] = "Slack Çalışma Alanımıza Davetlisin! 🚀"

#         body = f"""
#         Merhaba,
        
#         Seni Slack çalışma alanımıza bekliyoruz. 
#         Aşağıdaki linke tıklayarak hemen kayıt olabilir ve aramıza katılabilirsin:
        
#         👉 {SLACK_INVITE_LINK}
        
#         Görüşmek üzere!
#         Bot Yöneticisi
#         """
#         msg.attach(MIMEText(body, 'plain'))

#         # Gmail sunucusuna bağlan
#         server = smtplib.SMTP('smtp.gmail.com', 587)
#         server.starttls()
#         server.login(GMAIL_USER, GMAIL_PASSWORD)
#         text = msg.as_string()
#         server.sendmail(GMAIL_USER, gidecek_adres, text)
#         server.quit()
        
#         print(f"✅ Davetiye gönderildi: {gidecek_adres}")
        
#     except Exception as e:
#         print(f"❌ Hata ({gidecek_adres}): {e}")

# # --- TOPLU GÖNDERİM ---
# print("📨 Toplu davet gönderimi başlıyor...")
# for email in davet_listesi:
#     davetiye_gonder(email)
# print("🏁 İşlem tamamlandı.")