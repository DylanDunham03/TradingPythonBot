import os
import numpy
import alpaca_trade_api as api
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY_ID")
API_SECRET = os.getenv("API_SECRET_KEY_ID")
# print(API_KEY, API_SECRET)
BASE_URL = "https://paper-api.alpaca.markets"

alpaca = api.REST(API_KEY, API_SECRET, BASE_URL)
account = alpaca.get_account()
# print(account)

print("---------------------")

#os.getenv('') -> to get stuff from environment

# order = alpaca.submit_order(
# 	symbol='GOOGL',
# 	qty=1,
# 	side='buy',
# 	time_in_force='ioc')
# print(order)

# positions = alpaca.list_positions()
# for position in positions:
    # print(position)

# print(order)

print("----------------------------------")