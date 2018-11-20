import codecs
import configparser


class Parser:
    def __init__(self):
        self.configfile = './config/config.ini'

        config = configparser.ConfigParser()
        config.read_file(codecs.open(self.configfile, "r", "utf-8-sig"))

        self.api_key = config['Binance']['API_Key']
        self.secret = config['Binance']['Secret']

