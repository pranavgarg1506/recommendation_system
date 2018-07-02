#!/usr/bin/python3


from flask import Flask,render_template,request,session
import mysql.connector as mariadb

def person_recommend_page(uid):
	uid = int(uid[0][0])
	mariadb_connection = mariadb.connect(user='pranav', password='funny', database='major', host='localhost')
	if mariadb_connection.is_connected():
		cursor = mariadb_connection.cursor()
		
		#FETCHING BOOKS FOR USER 		(===USER_RATING===)
		#uid=input('Enter the user id : ')
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
		
		#TWO-STAGE MAJOR RECOMMENDATION	
		major_recommendation=recommended_bid_gerne+recommended_bid_author
		
		
		##RECOMMEND STAGE 3 -- IF AUTHOR DISLIKES BOTH AUTHOR AND GERNE THAT HE LIKES	
		
		#FETCHING POPULAR BOOKS INSTEAD
		recommended_bid_maduser=[]
		bad_author=[]
		bad_gerne=[]
		for i in range(len(book_details)):
			author_liked=book_details[i][1]	
			gerne_liked=book_details[i][2]	
			#print(author_liked)
			if author_liked in author_dislike and gerne_liked in gerne_dislike:
				bad_author.append(author_liked)
				bad_gerne.append(gerne_liked)
		
		#MAKING STRING
		bad_gerne_str='""'
		for i in range(len(bad_gerne)):
			bad_gerne_str=bad_gerne_str+',"'+bad_gerne[i]+'"'
		
		bad_author_str='""'
		for i in range(len(bad_author)):
			bad_author_str=bad_author_str+',"'+bad_author[i]+'"'
	
		
		#FETCHING OTHER AUTHORS
		cursor.execute('SELECT b_id,b_name,b_author,b_type,b_avg_rating from books_details where b_type not in ('+bad_gerne_str+')')
		det1 = cursor.fetchall()
		
		#FETCHING OTHER GERNES
		cursor.execute('SELECT b_id,b_name,b_author,b_type,b_avg_rating from books_details where b_author not in ('+bad_author_str+')')
		det2 = cursor.fetchall()
		
		stage3_recommendation=[]
		for i in range(0,len(det1)):
			stage3_recommendation.append(det1[i])
		for i in range(0,len(det2)):
			if det2[i] not in stage3_recommendation:
				stage3_recommendation.append(det2[i])
		
		#SORTING ACC TO GLOBAL RATING
		stage3_recommendation.sort(key = lambda x: x[4])
		stage3_recommendation.reverse()
		
		
		#MARKING FOR HIT OF 5
		length_major=len(major_recommendation)
		final_recommendation=[]
		if length_major<5:
			for i in range(len(major_recommendation)):
				final_recommendation.append(major_recommendation[i])
			for i in range(len(stage3_recommendation)):
				if stage3_recommendation[i] not in final_recommendation:
					final_recommendation.append(stage3_recommendation[i])
			final_recommendation=final_recommendation[:5]
		else:
			final_recommendation=major_recommendation[:5]
	
				
		
		#RETURN FINAL RECOMMENDATION
		final_books = []	
		for i in final_recommendation:
			final_books.append(i[0:2])

		return final_books
