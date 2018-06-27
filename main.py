#!/usr/bin/python3


from flask import Flask,render_template,request,session
import mysql.connector as mariadb
from register import register_page
from login import login_page

mariadb_connection = mariadb.connect(user='pranav', password='funny', database='major', host='localhost')
cursor = mariadb_connection.cursor()

#______________________________________________________________________________________________________________________________

app = Flask(__name__)

#_______________________________________________________________________________________________________________________________


@app.route('/')
def home():
	return render_template('home.html')




@app.route('/register', methods=['GET', 'POST'])
def reg():
	return render_template('register.html')


@app.route('/add_data', methods=['GET', 'POST'])
def add():
	register_page()
	return render_template('login.html')





@app.route('/login', methods=['GET', 'POST'])
def log():
	return render_template('login.html')


@app.route('/check_data', methods=['GET', 'POST'])
def check():
	answer = login_page()
	if answer==1:
		return render_template('home.html')
	else:
		return render_template('login.html')



#____________________________________________________________________________________________________________________________________


if __name__ == '__main__':
	app.run(host='192.168.43.168',debug = True)

#app.run(host, port, debug, options)
