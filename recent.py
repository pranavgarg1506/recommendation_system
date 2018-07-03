#!/usr/bin/python3
import MySQLdb
import os
import datetime
db= MySQLdb.connect(host="localhost", user="root", passwd="", db="major")
cur = db.cursor()
a=datetime.date.today()
b=(a-datetime.timedelta(days=30))
c=b.strftime("%y %m %d")
d= c.split()
e=int("20"+d[0])
f=int(d[1])
g=int(d[2])
print(str(e)+", "+str(f)+", "+str(g))
#x=datetime.date("int("+str(e)+"), int("+str(f)+"), int("+str(g)+")")
#print(x)
cur.execute("SELECT * from books_details WHERE publish_date>STR_TO_DATE('"+str(f)+", "+str(g)+", "+str(e)+"', '%m, %e, %Y')")
res=cur.fetchall()
print(res)

