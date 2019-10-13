<p align="center"><img src="https://streamlending.com.au/wp-content/uploads/2018/01/SL-Loan-Hero-AI-logo-banks-300x264.png" width="128px"><p>

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
![Python](https://img.shields.io/badge/python-v3.6-blue.svg)
![Dependencies](https://img.shields.io/badge/dependencies-up%20to%20date-brightgreen.svg)
[![GitHub Issues](https://img.shields.io/github/issues/anfederico/flaskex.svg)](https://github.com/Eduzc07/flaskex/issues)
![Contributions welcome](https://img.shields.io/badge/contributions-welcome-orange.svg)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/ef2f8f65c67a4043a9362fa6fb4f487a)](https://www.codacy.com/app/RDCH106/Flaskex?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=RDCH106/Flaskex&amp;utm_campaign=Badge_Grade)


<!-- <p align="center"><img src="https://raw.githubusercontent.com/anfederico/Flaskex/master/media/flaskex-demo.png" width="100%"><p> -->

# Midterm Homework - StylexAI
Simple Web app using Style Transfer and has been deployed using Google Cloud and can be tested here in
[StylexAI](https://stylexai.appspot.com/).

This is in Beta version, it runs Ok in local host but have some troubles in Google Clouds. With free version can process images, but with pay-access can download the result.

## Homework features
- Machine learning in [Style Transfer](https://towardsdatascience.com/style-transfer-styling-images-with-convolutional-neural-networks-7d215b58f461)
- User login/signup functionality using [Flaskex](https://github.com/anfederico/Flaskex)
- Payment service using paypal

## Features
- Encrypted user authorizaton
- Database initialization
- New user signup
- User login/logout
- User settings
- Modern user interface
- Bulma framework
- Limited custom css/js
- Easily customizable
- Paid user using PayPal
- Style Transfer example

## Setup
```
git clone https://github.com/Eduzc07/machinelearning
cd machinelearning/5_midterm_StylexAI
pip install -r requirements.txt
python main.py
```

## Setup Google cloud to deploy
```
git clone https://github.com/Eduzc07/machinelearning
cd machinelearning/5_midterm_StylexAI
virtualenv --python python3  ~/envs/stylex
source ~/envs/stylex/bin/activate
pip install -r requirements.txt
# Test if it is running
python main.py
# Ignore if it has been already created
gcloud app create
# Change timeout
gcloud config set app/cloud_build_timeout 1200
# Deploy
gcloud app deploy app.yaml --project stylexai --http-timeout=1200 --verbosity=debug
```

## Links
- [Set Paypal Button](https://developer.paypal.com/docs/archive/checkout/integrate/#1-get-the-code)
- [Customize the PayPal JavaScript SDK Script](https://developer.paypal.com/docs/checkout/reference/customize-sdk/)
- [Yaml Validator](http://www.yamllint.com/)
