# from web3 import Web3

# url = 'http://127.0.0.1:7545'

# web3 = Web3(Web3.HTTPProvider(url))
# print(web3.isConnected())

# a = web3.eth.account.create()
# print(a.address)


from flask import Flask

UPLOAD_FOLDER = '/home/arnab/Desktop/Dapp/uploads'

app = Flask(__name__)
app.secret_key = "secret key"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024