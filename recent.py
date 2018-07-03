#!/usr/bin/python3
import MySQLdb
import os
import datetime
#database connection
db= MySQLdb.connect(host="localhost", user="root", passwd="", db="major")
cur = db.cursor()
#current date
tday=datetime.date.today()
#date 1 month ago
pday=(tday-datetime.timedelta(days=30))
final_pday=pday.strftime("%y %m %d")
split_pday= final_pday.split()
year="20"+split_pday[0]
month=split_pday[1]
date=split_pday[2]
#extracting name of books uploaded in ecent month
cur.execute("SELECT b_name from books_details WHERE publish_date>STR_TO_DATE('"+month+", "+date+", "+year+"', '%m, %e, %Y')")
res=cur.fetchall()
#printing books names
print(res)

