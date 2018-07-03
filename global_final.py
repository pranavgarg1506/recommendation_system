#!/usr/bin/python3

import mysql.connector as mariadb

#--------database connectivity---------------
mariadb_connection = mariadb.connect(user='akdixit', password='ad123', database='major', host='127.0.0.1')
cur = mariadb_connection.cursor()

books=['Fiction','Romance','Thriller','Adventures']
print(books)

#------book name---------
user_input=input("enter the book name")
user_rating=input("enter the rating")
user_rating=float(user_rating)
count=1
#------rating------
def rating():
	query='SELECT b_avg_rating from books_details where b_name=%s'
	cur.execute(query,(user_input,))
	out_rating=cur.fetchall()
	print(out_rating)
	avg_rating=(float(out_rating[0][0])+user_rating)/2

	query1='UPDATE books_details set b_avg_rating=%s where b_name=%s'
	cur.execute(query1,(avg_rating,user_input,))
	mariadb_connection.commit()
	print(avg_rating)
	print(count)

	
rating()

#--------------------recommendation-----------------
all_rating=[]
#----------overall recommendation----------------
def recommend():
	query='SELECT b_avg_rating from books_details'
	cur.execute(query)
	out=cur.fetchall()
	for i in range(0,len(out)):
		all_rating.append(out[i][0])

	all_rating.sort(key=float , reverse=True)

	for j in all_rating:
		query='SELECT b_name from books_details where b_avg_rating >=3.0 order by b_avg_rating DESC LIMIT 3'
		#query='SELECT b_name from books_details order by b_avg_rating limit 5'
		cur.execute(query)
		data=cur.fetchall()


	# final recommended book
	for i in range(0,len(data)):
		rec_book=data[i][0]
		print(rec_book)
	


#-------------------recommendation acc to type-----------------------------
t_rating=[]
bookdict=[]

def recommend_type():
	#ch = input("enter the book type")
	query2='SELECT b_type from books_details where b_name=%s'
	cur.execute(query2,(user_input , ))
	book_type=cur.fetchall()

	query ='SELECT b_avg_rating from books_details where b_type=%s'
	cur.execute(query,(book_type[0][0],))
	output = cur.fetchall()

	#print(book_type[0][0])

#comapring the type of book reader reads with the type of books we have
# 	for i in range(0,len(books)):
# 		if books[i]== book_type:
# 			print(books[i])

	for i in range(0,len(books)):
		if books[i] == book_type[0][0]:
			for j in range(0,len(output)):
				book=output[j][0]
				#print(book)

				t_rating.append(book)
			t_rating.sort(key=float , reverse=True)


	#print(t_rating)
	#print(bookdict)

	#--------now finding the book names from the database acc to rating
	

	for j in t_rating:
			query='SELECT b_name from books_details where b_avg_rating >=3.0 and b_type=%s order by b_avg_rating DESC LIMIT 2'
			#query='SELECT b_name from books_details order by b_avg_rating limit 5'
			cur.execute(query,(book_type[0][0],))
			data=cur.fetchall()
	
	# final recommended book
	for i in range(0,len(data)):
		rec_book=data[i][0]
		print(rec_book)


#menu for performing the given operation

option ='''	1. take Average rating
			2. Recommend overall
			3. Recommend acc to type
		'''
print(option)

choice = input("enter your choice")

if choice == '1':
	rating()

elif choice == '2':
	recommend()

elif choice == '3':
	recommend_type()
else:
	print("wrong choice !!!")












