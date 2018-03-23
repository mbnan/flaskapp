from flask import json_available

import db_helper,json

from bson.json_util import dumps
import json

def get_userList():
    results = db_helper.fetch_user_list()
    json_str = dumps(results)
    dict = json.loads(json_str)
    #print(len(dict))
    return json_str

def register_user(user,password,email,address):
    record_id = db_helper.save_user(user,password,email,address)
    msg = " "

    if record_id is not None:
        msg = "User " + user + " registered successfully. Please login"
    else:
        msg = "Failed to register user"
    print(msg)
    return msg

def get_creds_for_user(username):
    json_string = db_helper.fetch_creds_for_user(username)
    print(json_string)
    dict = json.loads(json_string)
    print(dict["name"])
    return dict