from flask import render_template

def display_login_page():
    return render_template('login1.html')


def display_about_page():
    return render_template('about.html')

def display_home_page():
    return render_template('home.html')

def login_success_page():
    return render_template('success.html')