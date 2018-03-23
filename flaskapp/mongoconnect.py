from pymongo import MongoClient
import user

#client connection
client = MongoClient('mongodb://localhost:27017')

def fetch_users():
    #Access DB and collection
    db_connection = client['flaskdb'].users

    results = db_connection.find()

    user_list = []
    print('results: ', results)
    for userdoc in results:
        user_record = user.user(userdoc['id'], userdoc['name'],  userdoc['password'],  userdoc['email'], userdoc['regdate'], userdoc['address'])
        user_list.append(user_record)
        print(user_list)
    return user_list

client.close()

#user connection pooling
#add try catch blocks
#read db config from config file
