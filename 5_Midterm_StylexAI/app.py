# -*- coding: utf-8 -*-

from scripts import tabledef
from scripts import forms
from scripts import helpers
from scripts import transfer

from PIL import Image

from flask import Flask, redirect, url_for, render_template, request, session
from werkzeug.utils import secure_filename

import json
import sys
import os

# VERIFY_URL_PROD = 'https://ipnpb.paypal.com/cgi-bin/webscr'
# VERIFY_URL_TEST = 'https://ipnpb.sandbox.paypal.com/cgi-bin/webscr'
# VERIFY_URL = VERIFY_URL_TEST

app = Flask(__name__)
app.secret_key = os.urandom(12)  # Generic key for dev purposes only

# Heroku
#from flask_heroku import Heroku
#heroku = Heroku(app)

# ======== Routing =========================================================== #
# -------- Login ------------------------------------------------------------- #
@app.route('/', methods=['GET', 'POST'])
def login():
    if not session.get('logged_in'):
        form = forms.LoginForm(request.form)
        if request.method == 'POST':
            username = request.form['username'].lower()
            password = request.form['password']
            if form.validate():
                if helpers.credentials_valid(username, password):
                    session['logged_in'] = True
                    session['username'] = username
                    return json.dumps({'status': 'Login successful'})
                return json.dumps({'status': 'Invalid user/pass'})
            return json.dumps({'status': 'Both fields required'})
        return render_template('login.html', form=form)
    user = helpers.get_user()
    return render_template('home.html', user=user)

@app.route("/logout")
def logout():
    session['logged_in'] = False
    return redirect(url_for('login'))


# -------- Signup ---------------------------------------------------------- #
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if not session.get('logged_in'):
        form = forms.LoginForm(request.form)
        if request.method == 'POST':
            username = request.form['username'].lower()
            password = helpers.hash_password(request.form['password'])
            email = request.form['email']
            orderID = request.form['orderID']
            print("======================================")
            print(orderID)
            print("======================================")
            if form.validate():
                if not helpers.username_taken(username):
                    helpers.add_user(username, password, email, orderID)
                    session['logged_in'] = True
                    session['username'] = username
                    return json.dumps({'status': 'Signup successful'})
                return json.dumps({'status': 'Username taken'})
            return json.dumps({'status': 'User/Pass required'})
        return render_template('login.html', form=form)
    return redirect(url_for('login'))


# -------- Settings ---------------------------------------------------------- #
@app.route('/settings', methods=['GET', 'POST'])
def settings():
    if session.get('logged_in'):
        if request.method == 'POST':
            password = request.form['password']
            if password != "":
                password = helpers.hash_password(password)
            email = request.form['email']
            helpers.change_user(password=password, email=email)
            return json.dumps({'status': 'Saved'})
        user = helpers.get_user()
        return render_template('settings.html', user=user)
    return redirect(url_for('login'))

# ------------------ PayPal ----------------------------------------
# def get_current_user_id():
#     return '77777'
#
#
# @app.route("/")
# def buy_page():
#     return render_template('index.html', user_id=get_current_user_id())
#

# @app.route("/paypal_ipn", methods=['POST', 'GET'])
# def paypal_ipn_listener():
#     print("IPN event received.")
#
#     # Sending message as-is with the notify-validate request
#     params = request.form.to_dict()
#     params['cmd'] = '_notify-validate'
#     headers = {'content-type': 'application/x-www-form-urlencoded',
#                'user-agent': 'Paypal-devdungeon-tester'}
#     response = requests.post(VERIFY_URL, params=params, headers=headers, verify=True)
#     response.raise_for_status()
#
#     # See if PayPal confirms the validity of the IPN received
#     if response.text == 'VERIFIED':
#         print("Verified IPN response received.")
#         try:
#             user_id_of_buyer = params['custom'].split(":")[1]
#             print("User who bought item: " + str(user_id_of_buyer))
#
#             # Take action, e.g. update database to give user 1000 tokens
#
#         except Exception as e:
#             print(e)
#
#     elif response.text == 'INVALID':
#         # Don't trust
#         print("Invalid IPN response.")
#     else:
#         print("Some other response.")
#         print(response.text)
#     return ""
#
#
# @app.route("/paypal_cancel")
# def paypal_cancel():
#     return "PayPal cancel"


@app.route("/paypal_success", methods=['GET', 'POST'])
def paypal_success():
    if session.get('logged_in'):
        if request.method == 'POST':
            orderID = request.form['orderID']
            helpers.change_user(orderID=orderID)
            return json.dumps({'status': 'Saved'})
        user = helpers.get_user()
        return render_template('settings.html', user=user)
    return redirect(url_for('login'))

@app.route('/predict', methods=['GET', 'POST'])
def upload():
    print("---Upload!")
    if request.method == 'POST':
        print("------- Upload POST!")

        # Get the file from post request
        f = request.files['image']

        # Save the file to ./uploads
        basepath = os.path.dirname(__file__)
        file_path = os.path.join(
            basepath, 'uploads', secure_filename(f.filename))
        f.save(file_path)

        img = Image.open(request.files['image'].stream)
        rgb_im = img.convert('RGB')
        fileName = transfer.model_transfer(rgb_im)
        return fileName
    return None

@app.route('/style', methods=['GET', 'POST'])
def setStyle():
    print("-------------setStyle")
    if request.method == 'POST':
        namePath = request.data
        print(namePath)
        transfer.setStylePath(namePath)
    return 'Ok'

@app.route('/iteration', methods=['GET', 'POST'])
def setIteration():
    print("-------------iteration")
    if request.method == 'POST':
        iter = request.data
        print(iter)
        transfer.setIteration(iter)
    return 'Ok'

# @app.after_request
# def add_header(response):
#     """
#     Add headers to both force latest IE rendering engine or Chrome Frame,
#     and also to cache the rendered page for 10 minutes.
#     """
#     response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
#     response.headers['Cache-Control'] = 'public, max-age=0'
#     return response

# ======== Main ============================================================== #
if __name__ == "__main__":
    app.run(debug=True, use_reloader=True)
