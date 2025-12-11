import logging

# Loglama ayarlarını yapma
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%H:%M:%S'
)

def get_logger(name):
    #Her dosya icin ozel bir log kayitcisi olusturur.
    return logging.getLogger(name)
