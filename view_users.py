#!/usr/bin/python3

from flask import Flask,render_template,request,session
import mysql.connector as mariadb

def view_users_page():
	
	#connection
	mariadb_connection = mariadb.connect(user='pranav', password='funny', database='major', host='localhost')
	if mariadb_connection.is_connected():
		cursor = mariadb_connection.cursor()
		cursor.execute('SELECT * from user_details')
		result_users = cursor.fetchall()
		return result_users
