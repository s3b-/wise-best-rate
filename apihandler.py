#!/usr/local/bin/python3
import requests, os, configparser, json, uuid

path = os.path.dirname(os.path.abspath(__file__)) # path to this .py file
config = configparser.ConfigParser()
config.read(path + '/config.ini')
apiUrl = config.get('api', 'liveurl')
headers = {}
headers['Content-type'] = 'application/json'
headers['Authorization'] = 'Bearer ' + config.get('wise', 'apiKey')

def createQuote():
	data = {}
	data['sourceCurrency'] = config.get('currency', 'source')
	data['targetCurrency'] = config.get('currency', 'target')
	data['sourceAmount'] = config.get('currency', 'amount')
	data['targetAmount'] = None
	data['profile'] = config.get('wise', 'profile')
	response = requests.post(apiUrl + '/v2/quotes', data=json.dumps(data), headers=headers)
	answer = response.json()
	return answer['id']

def createTransfer(quoteUuid):
	data = {}
	data['targetAccount'] = config.get('wise', 'targetAccount')
	data['quoteUuid'] = quoteUuid
	data['customerTransactionId'] = str(uuid.uuid4())
	response = requests.post(apiUrl + '/v1/transfers', data=json.dumps(data), headers=headers)
	print(response.json())

createTransfer(createQuote())


