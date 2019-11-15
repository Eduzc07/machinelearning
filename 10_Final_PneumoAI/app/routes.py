# -*- coding: utf-8 -*-
from app import app # Import app to use routes

from app.scripts import tabledef
from app.scripts import forms
from app.scripts import helpers
from model_deploy import * # Import to build the model and predict a image

from PIL import Image

from flask import Flask, redirect, url_for, render_template, request, session

from werkzeug.utils import secure_filename

import json
import sys
import os

model = build_model() # Build the model with the specific json and h5 weights file

# VERIFY_URL_PROD = 'https://ipnpb.paypal.com/cgi-bin/webscr'
# VERIFY_URL_TEST = 'https://ipnpb.sandbox.paypal.com/cgi-bin/webscr'
# VERIFY_URL = VERIFY_URL_TEST

#app = Flask(__name__)
app.secret_key = os.urandom(12)  # Generic key for dev purposes only

# Heroku
#from flask_heroku import Heroku
#heroku = Heroku(app)

# Define the allowed file extensions that can be uploaded
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])

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

def allowed_file(filename):
	return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/predict', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        # Get the file from post request
        file = request.files['image']
        if file and allowed_file(file.filename):
            predictions = predict_image(model, file)
        return predictions
    return None
