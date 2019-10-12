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
    if request.method == 'POST':
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
    if request.method == 'POST':
        namePath = request.data
        transfer.setStylePath(namePath)
    return 'Ok'

@app.route('/iteration', methods=['GET', 'POST'])
def setIteration():
    if request.method == 'POST':
        iter = request.data
        transfer.setIteration(iter)
    return 'Ok'

# ======== Main ============================================================== #
if __name__ == "__main__":
    # app.run(use_reloader=True)
    # app.run(debug=True, use_reloader=True)
    app.run(host= '0.0.0.0', use_reloader=True)
