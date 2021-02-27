from pymongo import MongoClient

# Connect db
cluster = MongoClient('mongodb+srv://vk_bot:H2CqNIikM6gs7fil@chibi.gprgc.mongodb.net/vk_bot?retryWrites=true&w=majority')
db = cluster['vk_bot']
collection = db['chibi']

# list info user
info_list = []

def get_info_user():
    connect_get_info = collection.find()
    for i in connect_get_info:
        info_list.append(i)
    return info_list

def check_register_user(user_id):
    if collection.count_documents({'_id': user_id}) == 0:
        return False
    else:
        return True

def register_user(user_id):
       if collection.count_documents({'_id': user_id}) == 0:
            collection.insert_one({"_id":user_id})

#def register_user():
#    get_info_user()

#x = {'_id': 2, 'balance:': 5}



#collection.insert_one({"_id":3, "name": 'lol'})