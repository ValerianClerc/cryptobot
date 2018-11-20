from config import parser
#from binance.client import Client

print('Running bot')

# Fetching data from config file:
config = parser.Parser()
print(config.api_key)
print(config.secret)
#client = Client(api_key, api_secret)

