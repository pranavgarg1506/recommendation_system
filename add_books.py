#!/usr/bin/python3

from flask import Flask,render_template,request,session
import mysql.connector as mariadb

def add_books_page():
	mariadb_connection = mariadb.connect(user='pranav', password='funny', database='major', host='localhost')
	if mariadb_connection.is_connected():
		cursor = mariadb_connection.cursor()

		# requesting the values from the form
		bname = request.form['b_name']
		bauthor = request.form['b_author']
		btype = request.form['b_type']
		brating = request.form['avg_rating']
		
		## inserting the values into the table
		cursor.execute("INSERT INTO books_details(b_name,b_author,b_type,b_avg_rating) VALUES (%s,%s,%s,%s)",(bname,bauthor,btype,brating))
		mariadb_connection.commit()
	else:
		return 'error'

