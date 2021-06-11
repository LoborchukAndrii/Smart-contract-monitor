from pymongo import MongoClient
from datetime import date


mongo = MongoClient('localhost', 27017)
Contract_collection = mongo.AuctionBot.Contracts
User_collection = mongo.AuctionBot.Users


def add_conract(address):
    if Contract_collection.find_one({'Contract_Address':address}) == None :
        today = date.today()
        d3 = today.strftime("%d/%m/%y")
        Contract_collection.insert_one({'Contract_Address':address, 'Date': d3, 'Ended': False, 'Buyer':'', 'Time':''})


def set_event_time(address, time):
    Contract_collection.update_one({'Contract_Address': address}, {"$set": {'Time': time}})


def contract_end(address,end):
    Contract_collection.update_one({'Contract_Address': address}, {"$set": {'Ended': end}})


def contract_buyer(address, buyer):
    Contract_collection.update_one({'Contract_Address': address['Contract_Address']}, {"$set": {'Buyer': buyer}})


def get_buyer(address):
    db_info = Contract_collection.find_one({'Contract_Address': address})
    if db_info is not None:
        return db_info['Buyer']



def get_contracts():
    contracts_db = []
    for i in Contract_collection.find():
        contracts_db.append(i['Date'])
    print(contracts_db)
    return contracts_db


def get_contracts_notification():
    return Contract_collection.find({'Ended':False})


def get_contract_by_date(date):
    contact = Contract_collection.find_one({'Date': date})
    return contact['Contract_Address']


def set_selected_contract(ID,address):
    User_collection.update_one({'User_ID': ID},{ "$set":{'Contract': address}})


def get_selected_contract(ID):
    user_info = User_collection.find_one({'User_ID': ID})
    if user_info is None or user_info['Contract'] == '':
        return 'Не обрано контракт'
    return user_info['Contract']


def is_admin(ID):
    user_info = User_collection.find_one({'User_ID': ID})
    if user_info is not None:
        if user_info['Admin']:
            return True
        else:
            return False
    else:
        return False


def get_address_key(ID):
    user_info = User_collection.find_one({'User_ID': ID})
    if user_info['Address'] is None or user_info['Address'] == '':
        return None
    else:
        return {'user_address': user_info['Address'], 'user_key': user_info['Key']}


def set_address(ID, key):
    user_info = User_collection.update_one({'User_ID': ID},{ "$set": {'Address': key}})


def set_key(ID, key):
    user_info = User_collection.update_one({'User_ID': ID},{ "$set": {'Key': key}})


def notification_all():
    users_id = []
    user_info = User_collection.find({'Notification': True})
    for i in user_info:
        users_id.append(i['User_ID'])
    return users_id


def set_notification(ID):
    User_collection.update_one({'User_ID': ID},{ "$set":{'Notification': True}})


def not_notification(ID):
    User_collection.update_one({'User_ID': ID},{ "$set":{'Notification': False}})


def add_user(ID):
    if User_collection.find_one({'User_ID':ID}) is None:
        User_collection.insert_one({
            'User_ID':ID,
            'Admin': False,
            'Notification': False,
            'Query': '',
            'Item': '',
            'Contract': '',
            'Address': '',
            'Key': ''})


def set_user_query(ID,query):
    User_collection.update_one({'User_ID': ID},{'$set':{'Query':query}})


def get_user_query(ID):
    user_info=User_collection.find_one({'User_ID': ID})
    return user_info['Query']


def set_user_item(ID,item):
    User_collection.update_one({'User_ID': ID}, {'$set': {'Item': item}})


def get_user_item(ID):
    user_info=User_collection.find_one({'User_ID': ID})
    return user_info['Item']
