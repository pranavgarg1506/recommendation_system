#!/usr/bin/python3

from flask import Flask,render_template,request,session
import mysql.connector as mariadb

def final_update_page(b_id, u_id, u_rate):
	mariadb_connection = mariadb.connect(user='pranav', password='funny', database='major', host='localhost')
	if mariadb_connection.is_connected():
		cursor = mariadb_connection.cursor()
		cursor.execute("SELECT check_rating from user_rating where p_id = "+str(u_id)+" and b_id = "+str(b_id)+"")
		name = cursor.fetchall()
		mariadb_connection.commit()
		
		status = 'unknown'
		
		if name==[]:
			cursor.execute("insert into user_rating values (%s,%s,%s,%s)",(str(u_id),str(b_id),str(u_rate),str(1)))			
			mariadb_connection.commit()
			cursor.execute("Select b_avg_rating,count from books_details where b_id = "+str(b_id)+"")
			result = cursor.fetchall()
			avg_rating = result[0][0]
			count = result[0][1]
			total = avg_rating * count
			new_count = count+1
			new_avg = float(((float(total) + float(u_rate))/(new_count)))

			cursor.execute("update books_details set b_avg_rating = %s , count = %s where b_id = %s",(str(new_avg),str(new_count),str(b_id)))
			mariadb_connection.commit()
