#!/usr/bin/python3


from flask import Flask,render_template,request,session,redirect, url_for
import mysql.connector as mariadb
from register import register_page
from login import login_page
from user import user_page
from admin_login import admin_login_page
from view_users import view_users_page
from view_books import view_books_page
from add_books import add_books_page
from person_recommend import person_recommend_page
from book import book_page
from rating_update import rating_update_page
from final_update import final_update_page


mariadb_connection = mariadb.connect(user='pranav', password='funny', database='major', host='localhost')
cursor = mariadb_connection.cursor()

#______________________________________________________________________________________________________________________________

app = Flask(__name__)
app.secret_key = os.urandom(24)

#_______________________________________________________________________________________________________________________________


@app.route('/')
def home():
	return render_template('home.html')






# ALL ABOUT USER REGISTER PAGE
@app.route('/register', methods=['GET', 'POST'])
def reg():
	return render_template('register.html')

@app.route('/add_data', methods=['GET', 'POST'])
def add():
	register_page()
	return render_template('login.html')







# ALL ABOUT USER LOGIN AND ITS OPERATION PAGE
@app.route('/login', methods=['GET', 'POST'])
def log():
	return render_template('login.html')

@app.route('/check_data', methods=['GET', 'POST'])
def check():
	answer = login_page()
	if answer[0]==1:
		name = user_page(answer[1])
		personal_books = person_recommend_page(answer[1])
		return render_template('user.html',uname=name,p_books=personal_books,id_u=answer[1][0][0])
	else:
		return render_template('login.html')





# ALL ABOUT PAGE DESCRIPTION
@app.route('/book_description<int:b_id><int:u_id>', methods=['GET', 'POST'])
def des(b_id,u_id):
	book_desc = book_page(b_id)
	return render_template('book.html',results=book_desc,u_id=u_id)




# ALL ABOUT BOOK RATING UPDATION
@app.route('/rate_update<int:b_id><int:u_id>', methods=['GET', 'POST'])
def update(b_id,u_id):
	u_rate = rating_update_page()
	final_update_page(b_id, u_id, u_rate)
	book_desc = book_page(b_id)
	return render_template('book.html',results=book_desc,u_id=u_id)





# ABOUT ADMIN INFORMATION AND PERMISSIONS
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
