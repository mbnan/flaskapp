import pymongo
from flask.json import jsonify
from pymongo import MongoClient, results

import random
from bson.json_util import dumps
import json
import datetime



import config


host = config.DATABASE_CONFIG['HOST']
port = config.DATABASE_CONFIG['PORT']
db_name = config.DATABASE_CONFIG['DB_NAME']
collection_name = config.DATABASE_CONFIG['USER_COLLECTION']
user_name = config.DATABASE_CONFIG['USER_NAME']
db_passwd = config.DATABASE_CONFIG['DB_PASSWORD']

client = MongoClient('mongodb://'+ host + ':'+ port + '/?connectTimeoutMS=300000&maxPoolSize=50')

def fetch_user_list():
    try:
        #mongo URI  + '/?connectTimeoutMS=300000'

        #client = MongoClient('mongodb://localhost:27017')
        #get database, collection
        db_connection = client[db_name].users
        results = db_connection.find()
        json_str = ''

        results = db_connection.find()

        return results

    except pymongo.errors.ConnectionFailure as e:
        print("Could not connect to server: ", e )

    finally:
        client.close()

def save_user(user,password,email,address):
    try:
        #save to DB
        db_connection = client["flaskdb"].users
        id = random.getrandbits(64)>>32
        date_time = datetime.datetime.now().strftime("%I:%M%p on %B %d, %Y")
        record_id = db_connection.save({"id":id, "name":user, "password":password,"email":email,"regdate":date_time,"address":address })

        return record_id

    except pymongo.errors.ConnectionFailure as e:
        print("Could not connect to server and save record: ", e)
    finally:
        client.close()

def fetch_creds_for_user(username):
    try:
        db_connection = client[db_name].users
        cursor = db_connection.find({"name":username})

        if cursor:
            for doc in cursor:
                json_string = dumps(doc)

    except pymongo.errors.ConnectionFailure as e:
        print("Could not connect to server and save record: ", e)
    finally:
        client.close()
    return json_string