import os
import urllib.request
from app import app
from flask import Flask, request, redirect, jsonify
from werkzeug.utils import secure_filename
import ipfsapi
from web3 import Web3
import firebase_admin
from firebase_admin import auth
from firebase_admin import credentials
from firebase_admin import db
import hashlib
import json
# from cryptography.fernet import Fernet


cred = credentials.Certificate('/home/arnab/Downloads/pyKey.json')

firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://dapp-ac62a.firebaseio.com'
})



####### CONSTANTS #################
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

url = 'http://127.0.0.1:7545'
web3 = Web3(Web3.HTTPProvider(url))
print("Connection Established",web3.isConnected())


abi = json.loads('[{"constant":true,"inputs":[{"name":"","type":"address"}],"name":"people","outputs":[{"name":"user","type":"string"},{"name":"_firstname","type":"string"},{"name":"_lastname","type":"string"},{"name":"addr","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"user","type":"string"},{"name":"_firstname","type":"string"},{"name":"_lastname","type":"string"},{"name":"addr","type":"address"}],"name":"addPerson","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"peopleCount","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"addr","type":"address"},{"name":"docType","type":"string"},{"name":"date","type":"string"},{"name":"content","type":"string"}],"name":"addDoc","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"name":"addr","type":"address"},{"name":"docType","type":"string"}],"name":"getDoc","outputs":[{"name":"name","type":"string"},{"name":"isVerified","type":"bool"},{"name":"date","type":"string"},{"name":"content","type":"string"}],"payable":false,"stateMutability":"view","type":"function"}]')

contract_address = web3.toChecksumAddress('0xbed09689e708968429cbc21ddd10a2f82952bf98')
contract = web3.eth.contract(address = contract_address , abi = abi)




# config = {
#     "apiKey": "AIzaSyCoB7c1zY8WCwTTxylo0Jic6OiyopbItK8",
#     "authDomain": "dapp-ac62a.firebaseapp.com",
#     "databaseURL": "https://dapp-ac62a.firebaseio.com",
#     "projectId": "dapp-ac62a",
#     "storageBucket": "dapp-ac62a.appspot.com",
#     "messagingSenderId": "741388296515",
#     "appId": "1:741388296515:web:6bf1b4074eb3a523f00ff6",
#     "measurementId": "G-TCMVHDF2RF",
#     "serviceAccount": "pyKey.json"
#   };
# firebase = pyrebase.initialize_app(config)
# auth = firebase.auth()
# db = firebase.database()


##############################################

def allowed_file(filename):
	return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/reqVerify', methods=['POST'])
def reqVer():

	no = request.form['no']
	dname = request.form['dname']
	asking_no = request.form['ask']
	password = request.form['pass']

	ref = db.reference('docs/'+str(no)+'/'+str(dname)+'/loc').get()
	ipfshash = ref['Hash']


	resp = jsonify({'message':"Hui gawa" , "flag":1 , "url":ipfshash})
	return resp

@app.route('/request', methods=['POST'])
def req():

	no = request.form['no']
	dname = request.form['dname']
	asking_no = request.form['ask']

	reqref = db.reference('requests/'+str(no))
	reqref.child(asking_no).set({
		'address':asking_no,
		'dname':dname,
		'name':"Main "
		})
	resp = jsonify({'message':"Hui gawa" , "flag":1})
	return resp

@app.route('/signup', methods=['POST'])
def signup():

	if 'email' not in request.form :
		resp = jsonify({'message' : "No user"})
		return resp

	if 'pass' not in request.form :
		resp = jsonify({'message' : "No pass"})
		return resp

	email = request.form['email']
	password = request.form['pass']
	name = request.form['name']
	no = request.form['no']
	# ref = db.reference('users')


	try :
		# user = auth.create_user(email=email,password = password)
		# print(user)


		try :
			new_acc = web3.eth.account.create()
			keystore = new_acc.encrypt(password)
			hashed = hashlib.sha256(password.encode()) 
			key = str(hashed.hexdigest())

			tx_hash = contract.functions.addPerson(no,name,email,web3.toChecksumAddress(new_acc.address))
			print(tx_hash)

			# try :

			# 	abi = json.loads('[{"constant":true,"inputs":[{"name":"","type":"address"}],"name":"people","outputs":[{"name":"user","type":"string"},{"name":"_firstname","type":"string"},{"name":"_lastname","type":"string"},{"name":"addr","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"user","type":"string"},{"name":"_firstname","type":"string"},{"name":"_lastname","type":"string"},{"name":"addr","type":"address"}],"name":"addPerson","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"peopleCount","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"addr","type":"address"},{"name":"docType","type":"string"},{"name":"date","type":"string"},{"name":"content","type":"string"}],"name":"addDoc","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"name":"addr","type":"address"},{"name":"docType","type":"string"}],"name":"getDoc","outputs":[{"name":"name","type":"string"},{"name":"isVerified","type":"bool"},{"name":"date","type":"string"},{"name":"content","type":"string"}],"payable":false,"stateMutability":"view","type":"function"}]')
			# 	address = web3.toCheckSumAddress(new_acc.address)


			# 	contract = web3.eth.contract(address = address , abi = abi)


			# print(new_acc)
			try :

				ref = db.reference('users')

				ref.child(no).set({
					'name' : name,
					'email' : email,
					'hashed' : key,
					'address':new_acc.address,

					'keystore' : keystore,
					'role' : 'User'
					})
			except Exception as e :
				print(e , "Fb error")
				resp = {'message':e }
				return resp

			resp = jsonify({'message' : "SUCESSS" , 'flag' : 1})
			return resp

			# data = {"address": new_acc.address , "keystore" : keystore}
			# db.child("users").child(email).set(data)
		except Exception as e:
			print(e , "Web3 Error")

			resp = jsonify({'message' : "Web3 Error" , 'flag' : 0})
			return resp





	except Exception as e :
		print(e , "error in Signup")
		resp = jsonify({'message' : "No pass"})
		return resp




@app.route('/login', methods=['POST'])
def login():

	if 'pass' not in request.form :
		resp = jsonify({'message' : "No pass"})

	no = request.form['no']
	password = request.form['pass']

	try :

		userpass = db.reference('users/'+str(no)).get()

		upass = userpass['hashed']
		hashed = hashlib.sha256(password.encode()) 
		hashed = str(hashed.hexdigest())
		if(hashed == upass):
			resp = jsonify({'message' : "Succes" , "flag":1})
			return resp
		else :
			resp = jsonify({'message' : "Wrong pass" , "flag":0})
			return resp


	except Exception as e :
		print(e , "Error in SIgnIn")
		resp = jsonify({'message' : "Sign In failed" , "flag":0})
		return resp



@app.route('/file-upload', methods=['POST'])
def upload_file():
	# check if the post request has the file part
	if 'file' not in request.files:
		resp = jsonify({'message' : 'No file part in the request'})
		resp.status_code = 400
		return resp
	file = request.files['file']
	# print(dir(request))
	# print(type(file))
	# print(dir(file))
	# print(file.filename)
	if file.filename == '':
		resp = jsonify({'message' : 'No file selected for uploading'})
		resp.status_code = 400
		return resp
	if file and allowed_file(file.filename):
		filename = secure_filename(file.filename)
		no = request.form['no']
		dname = request.form['dname']

		try:
			
			api = ipfsapi.connect('127.0.0.1', 5001)
			# print(api)
		except ipfsapi.exceptions.ConnectionError as ce:
			print(str(ce))

		try :
			u = db.reference('users/'+str(no)).get()
			uaddr = u['address']
		except Exception as e :
			print(e, "Errrrorr")
			resp = jsonify({'message' : 'FAIL1'})
			# resp.status_code = 201
			return resp
		try:

			docref =db.reference('docs')
			verref = db.reference('officials')
		except Exception as e :
			print(e, "Errrrorr")
			resp = jsonify({'message' : 'FAIL2'})
			# resp.status_code = 201
			return resp
		try:
			tx_hash = contract.functions.addDoc(web3.toChecksumAddress(uaddr) , dname , "today","content")
			print(tx_hash)

		except Exception as e:
			print(e , "Hage yaha")
			resp = jsonify({'message' : 'pppppppppp'})
			# resp.status_code = 201
			return resp


		try:

			new_file_hash = api.add(file)

			print("successfully")
			print(new_file_hash)

			verref.child(no).set(
				{
				'docType' : dname
				})


			docref.child(no).child(dname).set({
				'docType' : dname ,
				'loc' : new_file_hash,
				
				})
		except Exception as e :
			print(e, "Errrrorr")
			resp = jsonify({'message' : 'FAIL'})
			# resp.status_code = 201
			return resp


		# file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
		resp = jsonify({'message' : 'File successfully uploaded'})
		resp.status_code = 201
		return resp
	else:
		resp = jsonify({'message' : 'Allowed file types are txt, pdf, png, jpg, jpeg, gif'})
		resp.status_code = 400
		return resp



if __name__ == "__main__":
    app.run(port = 8000 , debug =True)
