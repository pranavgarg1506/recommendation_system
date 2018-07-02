#!/usr/bin/python3


from flask import Flask,render_template,request,session
import mysql.connector as mariadb


mariadb_connection = mariadb.connect(user='mak', password='pri1221', database='major', host='localhost')
if mariadb_connection.is_connected():
	cursor = mariadb_connection.cursor()
	
	#FETCHING BOOKS FOR USER   		(===USER_RATING===)
	#uid=input('Enter the user id : ')
	uid=1
	cursor.execute('SELECT * from user_rating where p_id = '+str(uid))
	user_details = cursor.fetchall()
	
	print(user_details)	#LIST OF TUPLES	(=UR=)
	print('\n')
	
	'''
	cursor.execute("INSERT INTO user_details(p_name,p_email,p_uname,p_pass) VALUES (%s,%s,%s,%s)",(name,email,user,pass1))
		mariadb_connection.commit()
	'''

	for i in range(len(user_details)):
		cursor.execute("update user_rating set check_rating = 1 where p_id="+str(uid)+" and b_id="+str(user_details[i][1])+"")
		mariadb_connection.commit()
		
		#FETCHING BOOK_DETAILS			(===BOOK_DETAILS===)
		cursor.execute('SELECT * from books_details where b_id='+str(user_details[i][1]))
		user_book_details = cursor.fetchall()
	
		#print(user_book_details)

		new_count=(user_book_details[0][6]+1)
		new_rating = (user_book_details[0][4] + user_details[i][2])/new_count

		#print(new_count)
		#print(new_rating)
		
		cursor.execute("update books_details set b_avg_rating = "+str(new_rating)+", count = "+str(new_count)+" where b_id="+str(user_details[i][1]))
		mariadb_connection.commit()

