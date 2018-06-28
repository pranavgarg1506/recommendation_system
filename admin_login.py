#!/usr/bin/python3

from flask import Flask,render_template,request,session
import mysql.connector as mariadb

def admin_login_page():
	flag = 0

	mariadb_connection = mariadb.connect(user='pranav', password='funny', database='major', host='localhost')
	if mariadb_connection.is_connected():
		cursor = mariadb_connection.cursor()
		check_admin_user = request.form['uname_admin']
		check_admin_pass = request.form['pass_admin']
		cursor.execute('SELECT a_uname from admin_details where a_uname = %s',[check_admin_user])
		result_users = cursor.fetchall()
		# check whether there is such username present or not
		if len(result_users) > 0:
			# if present CHECK FOR THE PASSWORD
			cursor.execute('SELECT a_pass from admin_details where a_uname = %s',[check_admin_user])
			result_password = cursor.fetchall()
			# validate the password
			if (result_password[0][0]==check_admin_pass):
				flag = 1
				return flag
			else:
				return flag
				
		else :
			return flag

		mariadb_connection.commit()
	else:
		return 'error'

				
