<p align="center"><img src="https://developer.nvidia.com/sites/default/files/akamai/homepage/DevZone_Icon_Green_Machine_Learning.png" width="128px"><p>

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
![Python](https://img.shields.io/badge/python-v3.6-blue.svg)
![Dependencies](https://img.shields.io/badge/dependencies-up%20to%20date-brightgreen.svg)
[![GitHub Issues](https://img.shields.io/github/issues/anfederico/flaskex.svg)](https://github.com/Eduzc07/flaskex/issues)
![Contributions welcome](https://img.shields.io/badge/contributions-welcome-orange.svg)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/ef2f8f65c67a4043a9362fa6fb4f487a)](https://www.codacy.com/app/RDCH106/Flaskex?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=RDCH106/Flaskex&amp;utm_campaign=Badge_Grade)


<!-- <p align="center"><img src="https://raw.githubusercontent.com/anfederico/Flaskex/master/media/flaskex-demo.png" width="100%"><p> -->

# Final Work - PneumoAI
Simple Web app using CNN has been deployed using Heroku and can be tested here in
[PneumoAI](https://pneumoai.herokuapp.com/).

The process can be checked in Google Colab.
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Eduzc07/machinelearning/blob/master/10_Final_PneumoAI/AutomatedDiagnosis.ipynb)


## Homework features
- Machine learning using [CNN](https://www.kaggle.com/faizunnabi/diagnose-pneumonia)
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
#### GitHub
```
git clone https://github.com/Eduzc07/machinelearning
cd machinelearning/10_Final_PneumoAI
pip install -r requirements.txt
python main.py
```
#### Heroku
```
git clone https://git.heroku.com/pneumoai.git
cd PneumoAI
pip install -r requirements.txt
python main.py
```

### Heroku Configuration
```
# To Create heroku project
heroku create pneumai --buildpack heroku/python
# Start git locally
git init
# Load libraries
pip freeze > requirements.txt
# Add remote
heroku git:remote -a pneumai
# To Deploy
git push heroku master
```

#### Example user SandBox Paypal
Use the next user to test PayPal:
```
e-mail: sb-pac4f384293@personal.example.com
pass: /CI.2hq[
```

## Links
- [Set Paypal Button](https://developer.paypal.com/docs/archive/checkout/integrate/#1-get-the-code)
- [Customize the PayPal JavaScript SDK Script](https://developer.paypal.com/docs/checkout/reference/customize-sdk/)
- [Lungcure](https://github.com/FlorianWoelki/lungcure)
- [Medical StartUp](https://github.com/namas191297/medical_cost_estimator_startup)

### Options to host Webapp
- [Render](https://render.com/)
- [Heroku](https://heroku.com)
