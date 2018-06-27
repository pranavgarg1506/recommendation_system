#!/usr/bin/python3

from flask import Flask,render_template,request,session
import mysql.connector as mariadb


def register_page():
	mariadb_connection = mariadb.connect(user='pranav', password='funny', database='major', host='localhost')
	if mariadb_connection.is_connected():
		cursor = mariadb_connection.cursor()
		name = request.form['name']
		email = request.form['email']
		user = request.form['username']
		pass1 = request.form['password']
		cursor.execute("INSERT INTO user_details(p_name,p_email,p_uname,p_pass) VALUES (%s,%s,%s,%s)",(name,email,user,pass1))
		mariadb_connection.commit()
	else:
		return 'error'

