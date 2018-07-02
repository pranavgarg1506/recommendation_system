#!/usr/bin/python3

from flask import Flask,render_template,request,session
import mysql.connector as mariadb

def book_page(b_id):
	print(type(b_id))
	mariadb_connection = mariadb.connect(user='pranav', password='funny', database='major', host='localhost')
	if mariadb_connection.is_connected():
		cursor = mariadb_connection.cursor()
		cursor.execute('SELECT * from books_details where b_id = %s',[b_id])
		name = cursor.fetchall()
		return name
