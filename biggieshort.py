import requests, json
from config import *

BASE_URL = APCA_API_BASE_URL
ACCOUNT_URL = '{}/v2/account'.format(BASE_URL)
ORDERS_URL = '{}/v2/orders'.format(BASE_URL)
POSITIONS_URL = '{}/v2/positions'.format(BASE_URL)
HEADERS = {'APCA-API-KEY-ID': APCA_API_KEY_ID, 'APCA-API-SECRET-KEY': APCA_API_SECRET_KEY}

def get_account():
    r = requests.get(ACCOUNT_URL, headers = HEADERS)
    
    return json.loads(r.content)

def create_order(symbol,qty,type,time_in_force):
    data = {
        'symbol': symbol,
        'qty': qty,
        'side': 'buy',
        'type': type,
        'time_in_force': time_in_force
    }

    r = requests.post(ORDERS_URL,json=data,headers = HEADERS)

    return json.loads(r.content)

def get_orders():
    r = requests.get(ORDERS_URL, headers = HEADERS)

    return json.loads(r.content)


def liquidate_order(symbol,qty,type,time_in_force):
    data = {
        'symbol': symbol,
        'qty': qty,
        'side': 'sell',
        'type': type,
        'time_in_force': time_in_force
    }

    r = requests.post(ORDERS_URL,json=data,headers = HEADERS)

    return json.loads(r.content)

def view_open():
    r = requests.get(POSITIONS_URL, headers = HEADERS)

    return json.loads(r.content)







# create_order('IYR','100','market','gtc')

response = view_open()
#get_orders()
print(response)