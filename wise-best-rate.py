#!/usr/local/bin/python3
from flask import Flask, render_template
import logging, os, configparser

app = Flask(__name__)

path = os.path.dirname(os.path.abspath(__file__)) # path to this .py file
config = configparser.ConfigParser()
config.read(path + '/config.ini')

@app.route('/')
def index():
    return render_template('index.html',
        configWiseProfile = config.get('wise', 'profile'),
        configCurrencySource = config.get('currency', 'source'),
        configCurrencyTarget = config.get('currency', 'target'),
        configCurrencyAmount = config.get('currency', 'amount')
        )