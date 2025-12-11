import logging

logger = logging.getLogger("UserCommands")

def emails_to_ids(client, email_list):

    valid_ids = []
    failed_emails = []
    
    for email in email_list:
        try:
            # Slack'e soruyoruz
            result = client.users_lookupByEmail(email=email.strip())
            valid_ids.append(result["user"]["id"])
        except Exception:
            failed_emails.append(email)
            
    return valid_ids, failed_emails

#Email ile id bulma
def get_id_by_email_func(client, email):
    try:
        result = client.users_lookupByEmail(email=email)
        return result["user"]["id"]
    except:
        return None

#İD ile email bulma
def get_email_by_id_func(client, user_id):
    try:
        result = client.users_info(user=user_id)
        return result["user"]["profile"].get("email")
    except:
        return None

#Kanala id ile davet etme
def invite_users_by_id_list(client, channel_id, user_id_list):
    try:
        users_str = ",".join(user_id_list)
        client.conversations_invite(channel=channel_id, users=users_str)
        return f"Şu kullanicilar eklendi: {users_str}"
    except Exception as e:
        return f"Ekleme hatasi: {e}"

#Kanala email ile davet etme
def invite_users_by_email_list(client, channel_id, email_list):
    # Önce e-postaları ID'ye çevir
    valid_ids, failed = emails_to_ids(client, email_list)
    
    if not valid_ids:
        return "Hiçbir e-posta geçerli bir kullanici ile eşleşmedi."
    
    msg = invite_users_by_id_list(client, channel_id, valid_ids)
    
    if failed:
        msg += f"\nŞu e-postalar bulunamadi: {', '.join(failed)}"
    return msg

#Kanaldan çıkarma
def kick_users_by_id_list(client, channel_id, user_id_list):
    success_count = 0
    errors = []
    
    for user_id in user_id_list:
        try:
            client.conversations_kick(channel=channel_id, user=user_id.strip())
            success_count += 1
        except Exception as e:
            errors.append(f"{user_id}: {e}")
            
    result_msg = f"✅ {success_count} kişi kanaldan çıkarıldı."
    if errors:
        result_msg += f"\n⚠️ Hatalar:\n" + "\n".join(errors)
    return result_msg

def kick_users_by_email_list(client, channel_id, email_list):
    # Önce ID'leri bul
    valid_ids, failed = emails_to_ids(client, email_list)
    
    if not valid_ids:
        return "❌ Bu e-postaların hiçbiri bulunamadı."
        
    # Bulunan ID'leri atma fonksiyonuna gönder
    msg = kick_users_by_id_list(client, channel_id, valid_ids)
    
    if failed:
        msg += f"\n⚠️ Bulunamayan E-postalar: {', '.join(failed)}"
    return msg
