# wise-best-rate
A web application to get the best possible Wise (aka Transferwise) rate

# Contribution
This project is in a very early phase, it will continuously grow during Hacktoberfest. Feel free to contribute! Please check the open issues to find out more.

# Installation
**If you run this application on a public server, protect it with e.g. BasicAuth!**
- Infall Flask: `pip3 install flask`
- Configure Flask:
  - `export FLASK_APP=wise-best-rate`
  - `export FLASK_ENV=development`
- To run webserver: `flask run`

# Configuration
- Rename `config.ini.template` to `config.ini`
  - Profile: Your profile ID, can be found with this [API endpoint](https://api-docs.wise.com/#payouts-guide-get-your-profile-id)
  -  apiKey: Set up [here](https://wise.com/settings/)
  -  targetAccount: ID of the target bank account, can be found e.g. by checking a existing transfer with [this endpoint](https://api-docs.wise.com/#transfers-list)

# Usage
The webinterace is currently pretty useless, it will grow n the next days. Currently everything happens by running `apihandler.py` e.g. via cronjob
