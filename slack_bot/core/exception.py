class BotError(Exception):
    """
    Bot projemizdeki tüm hatalarin atasi olan temel sinif.
    Diğer tüm özel hatalar buradan türetilir.
    """
    pass

class ConfigError(BotError):
    """
    .env dosyasi veya ayarlar ile ilgili hatalar için kullanilir.
    Örn: Token eksikse bu hata firlatilir.
    """
    pass

class SlackApiError(BotError):
    """
    Slack ile konuşurken bir sorun çikarsa bu hata kullanilir.
    Örn: İnternet kesildi, Token geçersiz vb.
    """
    pass

class CommandError(BotError):
    """
    Kullanicinin girdiği komut yanlişsa bu hata kullanilir.
    Örn: 'davet et' dedin ama ID girmedin.
    """
    pass