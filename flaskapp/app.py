#entry file
from flask import Flask,flash, render_template,request



import render_templates
import user_service
import json


from flask import jsonify


app = Flask(__name__)
app.secret_key = 'random string'

@app.route('/')
#render a template called index.html
def index():
    return render_templates.display_home_page()


@app.route('/about')
def about():

    return render_templates.display_about_page()

@app.route('/articles')
def articles():
    return render_template('articles.html')

@app.route('/login1', methods = ['GET','POST'])
def login():
    msg = None
    if request.method == 'POST':

        if request.form['username'] is not  None:
            input_username = request.form['username']
            input_password = request.form['password']

            user_dict = user_service.get_creds_for_user(input_username)
            #dict = json.loads(user_jsonStr)

            if user_dict["name"] == input_username  and user_dict["password"] == input_password:
                msg = 'You have Logged in Successfully'
                flash(msg,'message')
                return jsonify(dict(redirect='/',msg=msg))
            else:
                msg = 'Invalid credentials, Please try logging in again'
                flash(msg,'error')
                return jsonify(dict(redirect='/login1',msg=msg))
        else:
            msg = 'Please Enter User Name'
            flash(msg,'error')
            return jsonify(dict(redirect='/login1',msg=msg))
    elif request.method == 'GET':
        return render_templates.display_login_page()

@app.route('/users')
def list_users():
    user_dictionary = user_service.get_user_list()
    return render_template('user_list.html',userdict = user_dictionary)

@app.route('/usersInDB')
def display_users_from_mongo():
    user_json = user_service.get_userList()
    return user_json

@app.route('/userTest', methods = ['GET','POST'])
def users():
    if request.method == 'GET':
        return render_template('users.html')

@app.route('/register', methods = ['GET','POST'])
def registerUser():
    if request.method == 'GET':
        return render_template('registerUser.html')
    elif request.method == 'POST':
        user = request.form['username']
        password = request.form['password']
        email = request.form['email']
        address = request.form['address']
        msg = "User Saved Successfully. Please login "
        msg = user_service.register_user(user, password, email,address)
        flash(msg, 'message')

        return jsonify(dict(redirect='/login1',msg=msg))


if __name__ == '__main__':
    app.run(debug = True)
