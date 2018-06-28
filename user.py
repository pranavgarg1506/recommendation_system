#!/usr/bin/python3


from flask import Flask,render_template,request,session
import mysql.connector as mariadb

def user_page(uid):
	uid = int(uid[0][0])
	ans=[]
	mariadb_connection = mariadb.connect(user='pranav', password='funny', database='major', host='localhost')
	if mariadb_connection.is_connected():
		cursor = mariadb_connection.cursor()
		cursor.execute('SELECT p_name from user_details where p_id = %s', [uid])
		name = cursor.fetchall()
		ans1 = name[0][0]
		return name[0][0]
	
