#!/usr/bin/python3


from flask import Flask,render_template,request,session
import mysql.connector as mariadb


mariadb_connection = mariadb.connect(user='mak', password='pri1221', database='major', host='localhost')
if mariadb_connection.is_connected():
	cursor = mariadb_connection.cursor()
	
	#FETCHING BOOKS FOR USER 		(===USER_RATING===)
	uid=input('Enter the user id : ')
	cursor.execute('SELECT * from user_rating where p_id = '+str(uid))
	name = cursor.fetchall()
	
	#GETTING BOOK ID, RATING AND FORMING A DICTIONARY
	book_dict={}
	book_id=[]
	book_rating=[]
	book_id_dislike=[]
	for i in range(0,len(name)):
		#FILTERING THE GOOD RATINGS OF USER
		if name[i][2]>=3.0:		#(===AVG_GOOD_RATING===)
			book_dict[name[i][1]]=name[i][2]
			book_id.append(name[i][1])
			book_rating.append(name[i][2])
		else:
			book_id_dislike.append(name[i][1])
	#print(book_rating)
	#print(book_id)
	
	#FETCHING BOOK DETAILS FROM RATED BOOK ID  		(===BOOK_DETAILS===)
	book_details_label=[('book_id','author_name','gerne','avg_rating','user_rating')]
	book_details=[]
	for i in range(len(book_id)):	#LIKED BOOKS
		cursor.execute('SELECT b_id,b_author,b_type,b_avg_rating from books_details where b_id = '+str(book_id[i]))
		det = cursor.fetchall()[0]
		det = det + (book_rating[i],)
		book_details.append(det)
	#print(book_details)
	
	book_details_dislike=[]		#DISLIKED BOOKS
	for i in range(len(book_id_dislike)):
		cursor.execute('SELECT b_id,b_author,b_type,b_avg_rating from books_details where b_id = '+str(book_id_dislike[i]))
		det = cursor.fetchall()[0]
		book_details_dislike.append(det)
	
	##RECOMMEND STAGE 1 -- FROM GERNE	
		
	#SORTING ACC TO GLOBAL RATING
	book_details.sort(key = lambda x: x[3])
	#print (book_details_label)
	book_details.reverse()
	#print(book_details)
	
	#GERNE DISLIKED
	gerne_dislike=[]
	for i in book_details_dislike:
		gerne_dislike.append(i[2])	
	#print(gerne_dislike)
	
	#FETCHING GERNE FOR THE LIKED BOOK
	recommended_bid_gerne=[]
	for i in range(len(book_details)):
		gerne_liked=book_details[i][2]		
		#print(gerne_liked)
		if gerne_liked in gerne_dislike:
			continue
		else:
			#MAKING RECOMMENDATION
			#similar_book_gerne=[]	
			cursor.execute('SELECT b_id,b_name,b_author,b_type,b_avg_rating from books_details where b_type = "'+gerne_liked+'"')
			det = cursor.fetchall()
			det.sort(key = lambda x: x[4])
			det.reverse()
			if det[0] not in recommended_bid_gerne:
				recommended_bid_gerne.append(det[0])
				#print(det)

	
	##RECOMMEND STAGE 2 -- FROM AUTHOR	
		
	#AUTHOR DISLIKED
	author_dislike=[]
	for i in book_details_dislike:
		author_dislike.append(i[1])	
	#print(author_dislike)
	
	#FETCHING GERNE FOR THE LIKED BOOK
	recommended_bid_author=[]
	for i in range(len(book_details)):
		author_liked=book_details[i][1]		
		#print(author_liked)
		if author_liked in author_dislike:
			continue
		else:
			#MAKING RECOMMENDATION
			#similar_book_author=[]	
			cursor.execute('SELECT b_id,b_name,b_author,b_type,b_avg_rating from books_details where b_author = "'+author_liked+'"')
			det = cursor.fetchall()
			det.sort(key = lambda x: x[4])
			det.reverse()
			for i in range(len(det)):
				if det[i] not in recommended_bid_author:
					if det[i] not in recommended_bid_gerne:
						if det[i][0] not in book_id:
							recommended_bid_author.append(det[i])						
							break
			
	
	#PRINTING FINAL RECOMMENDATION	
	final_recommendation=recommended_bid_gerne+recommended_bid_author
	for i in final_recommendation:
		print(i)
	