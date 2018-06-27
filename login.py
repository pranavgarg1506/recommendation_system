#!/usr/bin/python3

from flask import Flask,render_template,request,session
import mysql.connector as mariadb



def login_page():	
	
	flag = 0
	
	#connection
	mariadb_connection = mariadb.connect(user='pranav', password='funny', database='major', host='localhost')
	if mariadb_connection.is_connected():
		cursor = mariadb_connection.cursor()
		check_user = request.form['username1']
		check_pass = request.form['password1']
		cursor.execute('SELECT p_uname from user_details where p_uname = %s',[check_user])
		result_users = cursor.fetchall()
		# check whether there is such username present or not
		if len(result_users) > 0:
			# if present CHECK FOR THE PASSWORD
			cursor.execute('SELECT p_pass from user_details where p_uname = %s',[check_user])
			result_password = cursor.fetchall()
			# validate the password
			if (result_password[0][0]==check_pass):
				flag = 1
				return flag
			else:
				return flag
				
		else :
			return flag

		mariadb_connection.commit()
	else:
		return 'error'

