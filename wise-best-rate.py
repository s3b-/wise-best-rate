#!/usr/local/bin/python3
from flask import Flask, render_template, request
import logging, os, configparser

def modifyConfig():
	if request.form.get('inputWiseSubmit'):
		print('Wise config')
	if request.form.get('inputCurrencySubmit'):
		print('Currency config')

app = Flask(__name__)

path = os.path.dirname(os.path.abspath(__file__)) # path to this .py file
config = configparser.ConfigParser()
config.read(path + '/config.ini')

@app.route('/', methods=['post', 'get'])
def index():

	if request.method == 'POST':
		modifyConfig()

	return render_template('index.html',
		configWiseProfile = config.get('wise', 'profile'),
		configWiseApiKey = config.get('wise', 'apiKey'),
		configWiseTargetAccount = config.get('wise', 'targetAccount'),
		configCurrencySource = config.get('currency', 'source'),
		configCurrencyTarget = config.get('currency', 'target'),
		configCurrencyAmount = config.get('currency', 'amount'),
		configEmailSmtpServer = config.get('email', 'SmtpServer'),
		configEmailSmtpPort = config.get('email', 'SmtpPort'),
		configEmailSmtpUser = config.get('email', 'SmtpUser'),
		configEmailSmtpPassword = config.get('email', 'SmtpPassword'),
		configEmailSmtpSender = config.get('email', 'SmtpSender'),
		configEmailRecipient = config.get('email', 'MailRecipient'),
		configEmailPrefix = config.get('email', 'MailPrefix'),
		configEmailEncryptionMode = config.get('email', 'EncryptionMode')
		)

def modifyConfig():
	if request.form.get('inputWiseSubmit'):
		config['wise']['profile'] = request.form.get('inputWiseProfile')
		config['wise']['targetAccount'] = request.form.get('inputWiseTargetAccount')
		config['wise']['apiKey'] = request.form.get('inputWiseApiKey')
		with open(path + '/config.ini', 'w') as configfile:
			config.write(configfile)

	if request.form.get('inputEmailSubmit'):
		config['email']['SmtpServer'] = request.form.get('inputEmailSmtpServer')
		config['email']['SmtpPort'] = request.form.get('inputEmailSmtpPort')
		config['email']['SmtpUser'] = request.form.get('inputEmailSmtpUser')
		config['email']['SmtpPassword'] = request.form.get('inputEmailSmtpPassword')
		config['email']['SmtpSender'] = request.form.get('inputEmailSmtpSender')
		config['email']['MailRecipient'] = request.form.get('inputEmailRecipient')
		config['email']['MailPrefix'] = request.form.get('inputEmailPrefix')
		config['email']['EncryptionMode'] = request.form.get('inputEmailEncryptionMode')
		with open(path + '/config.ini', 'w') as configfile:
			config.write(configfile)

	if request.form.get('inputCurrencySubmit'):
		print('Currency config')