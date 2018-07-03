#!/usr/bin/python3

from flask import Flask,render_template,request,session
import mysql.connector as mariadb

def rating_update_page():
	mariadb_connection = mariadb.connect(user='pranav', password='funny', database='major', host='localhost')
	if mariadb_connection.is_connected():
		cursor = mariadb_connection.cursor()
		

		user_rating = request.form['user_rating']
		return user_rating




















