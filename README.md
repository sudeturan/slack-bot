# 🤖 Slack Ofis Botu

Bu proje, Slack çalışma alanını yönetmek için geliştirilmiş Python tabanlı bir bottur. Kanal yönetimi, üye davet etme/çıkarma ve gelişmiş mesajlaşma özelliklerine sahiptir.

## 🚀 Özellikler

* **Kanal Yönetimi:** Kanal oluşturma ve arşivleme (silme).
* **Kişi Yönetimi:** E-posta ile ID bulma, ID ile E-posta bulma.
* **Üye İşlemleri:**
    * Kullanıcıları kanallara ekleme (Tekli veya Toplu Liste ile).
    * Kullanıcıları kanaldan çıkarma (Kick).
    * E-posta listesi kullanarak toplu davet.
* **Mesajlaşma:** Kanala, kişiye (DM) veya bir mesaja yanıt (Thread) olarak mesaj atma.

## 🛠 Kurulum

1.  Gerekli kütüphaneleri yükleyin:
    ```bash
    pip install -r requirements.txt
    ```

2.  `.env` dosyasını oluşturun ve Slack Token'larınızı girin:
    ```text
    SLACK_BOT_TOKEN=xoxb-...
    SLACK_APP_TOKEN=xapp-...
    ```

3.  Botu başlatın:
    ```bash
    python -m slack_bot.client
    ```

## 💬 Komut Listesi

Bot aşağıdaki komutlara yanıt verir:

| Görev | Komut Örneği |
| :--- | :--- |
| **Kanal Açma** | `kanal aç [Kanal-Adı]` |
| **Kanal Silme** | `kanal sil [Kanal-ID]` |
| **ID Bulma** | `id bul [email]` |
| **Email Bulma** | `email bul [User-ID]` |
| **Davet Etme (Email)** | `davet et email a@x.com,b@y.com [Kanal-ID]` |
| **Davet Etme (ID)** | `davet et id U123,U456 [Kanal-ID]` |
| **Kullanıcı Çıkarma** | `çıkar email a@x.com [Kanal-ID]` |
| **Mesaj Gönderme** | `mesaj gönder [Kanal/User ID] [Mesaj]` |
| **Thread Test Etme** | `thread` (Mesaja yanıt yazar) |

---
*Geliştirici: Sude Turan.*  -->

