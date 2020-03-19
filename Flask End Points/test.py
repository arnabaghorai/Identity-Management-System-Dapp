# from cryptography.fernet import Fernet

# message = "my deep dark secret".encode()

# f = Fernet("123")
# encrypted = f.encrypt(message)
# print(encrypted)


# import json
# from web3 import Web3


# url = 'http://127.0.0.1:7545'
# web3 = Web3(Web3.HTTPProvider(url))
# print("Connection Established",web3.isConnected())


# account_1 = '' # Fill me in
# account_2 = ''


# private_key = ''

# abi = json.loads('[{"constant":true,"inputs":[{"name":"","type":"address"}],"name":"people","outputs":[{"name":"user","type":"string"},{"name":"_firstname","type":"string"},{"name":"_lastname","type":"string"},{"name":"addr","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"user","type":"string"},{"name":"_firstname","type":"string"},{"name":"_lastname","type":"string"},{"name":"addr","type":"address"}],"name":"addPerson","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"peopleCount","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"addr","type":"address"},{"name":"docType","type":"string"},{"name":"date","type":"string"},{"name":"content","type":"string"}],"name":"addDoc","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"name":"addr","type":"address"},{"name":"docType","type":"string"}],"name":"getDoc","outputs":[{"name":"name","type":"string"},{"name":"isVerified","type":"bool"},{"name":"date","type":"string"},{"name":"content","type":"string"}],"payable":false,"stateMutability":"view","type":"function"}]')

# address = web3.toChecksumAddress('0xbed09689e708968429cbc21ddd10a2f82952bf98')

# # # address = '0x20de646C9674929873ae6d4cbBF163a8a1044B95'

# # # address = web3.toChecksumAddress(address)

# contract = web3.eth.contract(address = address , abi = abi)
# print(dir(contract))
# tx_hash = contract.functions.addPerson("abc","aa","aa",web3.toChecksumAddress('0xf16289701059E979648A104c6B6f4a7e6a32947C'))
# # tx_hash = contract.functions.addPerson("abc","aa","aa",address).transact()
# print(tx_hash)

# import firebase_admin
# from firebase_admin import credentials
# from firebase_admin import db

# # Fetch the service account key JSON file contents
# cred = credentials.Certificate('/home/arnab/Downloads/pyKey.json')

# # Initialize the app with a service account, granting admin privileges
# firebase_admin.initialize_app(cred, {
#     'databaseURL': 'https://dapp-ac62a.firebaseio.com'
# })


# # from firebase_admin import auth


# # print(dir(auth))
# # user = auth.get_user_by_email('jeeeet@gmail.com')
# # print('Successfully fetched user data: {0}'.format(user.uid))
# # print(dir(user))
# # print(user)

# # # As an admin, the app has access to read and write all data, regradless of Security Rules
# ref = db.reference('users/2222')
# print(ref.get()['hashed'])

# # ref.child('arnab').set({
# # 	'adress':"aaaa"

# # 	})



# # # import requests

# # # url = 'http://localhost:8080/ipfs/QmUmG5Zbqfg16LdbUUS6HwSazTBdY35BWdqGhHZ7tZMZ95'
# # # r = requests.get(url, allow_redirects=True)


# # # with open('a.jpeg', 'wb') as f:
# # # 	f.write(r.content)

import pyrebase

config = {
    "apiKey": "AIzaSyCoB7c1zY8WCwTTxylo0Jic6OiyopbItK8",
    "authDomain": "dapp-ac62a.firebaseapp.com",
    "databaseURL": "https://dapp-ac62a.firebaseio.com",
    "projectId": "dapp-ac62a",
    "storageBucket": "dapp-ac62a.appspot.com",
    "messagingSenderId": "741388296515",
    "appId": "1:741388296515:web:6bf1b4074eb3a523f00ff6",
    "measurementId": "G-TCMVHDF2RF",
    "serviceAccount": "/home/arnab/Downloads/service.json"
  };


firebase = pyrebase.initialize_app(config)
 
auth = firebase.auth()
email = "xyz@g.com"
password = "12345678"
# user = auth.create_user_with_email_and_password(email,password)

# print(user)
# print("----------------------------")
user = auth.sign_in_with_email_and_password(email, password)
print(dir(user))
# # #print(user)


# # # Global ID

# # # GlobalID = 1

# # # db = firebase.database()

# # # # Insert into database

# # # data = {
# # #     "UserUID" : user["localId"],
# # #     "GlobalID" : GlobalID  
# # # }
 
# # # # Pass the user's idToken to the push method
# # # results = db.child("users").push(data, user['idToken'])

# # # print(results)



# # # auth = firebase.auth()
 
# # # # Log the user in
# # # user = auth.sign_in_with_email_and_password(email, password)
 
# # # # Get a reference to the database service
# # # db = firebase.database()
 
# # # #retrieve Value
# # # users = db.child("users").get()
# # # print(users.val())
 
# # # #retrieve key
# # # user = db.child("users").get()
# # # print(user.key())
 
# # # #retrieve each
# # # all_users = db.child("users").get()
# # # for user in all_users.each():
# # #     print(user.key())
# # #     print(user.val())