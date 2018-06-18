# CryptoIntegrator
Web application showing integrated data about cryptocurrencies.

## Requirements
- Python 3.6 installed
- Twitter developer account
- Following environment variables need to be exported or filled out in file `config.py`:
  - CONSUMER_KEY
  - CONSUMER_SECRET
  - ACCESS_TOKEN_KEY
  - ACCESS_TOKEN_SECRET

## Installation
- `pip install -r ‘requirements.txt’`
- Recommended: setting up the virtual environment

## Running the application
- developer mode: `flask run`
- production mode: `gunicorn app:app`
