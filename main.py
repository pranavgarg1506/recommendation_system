#!/usr/bin/python3


from flask import Flask,render_template,request,session
import mysql.connector as mariadb
from register import register_page
from login import login_page
from user import user_page
from admin_login import admin_login_page
from view_users import view_users_page
from view_books import view_books_page
from add_books import add_books_page

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
	if answer[0]==1:
		name = user_page(answer[1])
		return render_template('user.html',uname=name)
	else:
		return render_template('login.html')




@app.route('/admin',methods=['GET','POST'])
def admin1():
	return render_template('admin/index.html')

@app.route('/check_data_admin', methods=['GET', 'POST'])
def check_admin():
	answer = admin_login_page()
	if answer==1:
		return render_template('admin/admin.html')
	else:
		return render_template('admin/index.html')

@app.route('/view_users', methods=['GET','POST'])
def show_view_users():
	users_info = view_users_page()
	return render_template('admin/view_users.html',results=users_info)

@app.route('/view_books', methods=['GET','POST'])
def show_view_books():
	books_info = view_books_page()
	return render_template('admin/view_books.html',results1=books_info)

@app.route('/add_books')
def addb():
	return render_template('admin/add_books.html')

@app.route('/add_books_data', methods=['GET', 'POST'])
def addbd():
	add_books_page()
	return render_template('admin/add_books.html')




#____________________________________________________________________________________________________________________________________


if __name__ == '__main__':
	app.run(host='192.168.43.168',debug = True)

#app.run(host, port, debug, options)
