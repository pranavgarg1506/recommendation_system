#!/usr/bin/env python3

#IMPORT LIBRARIES
from xlrd import open_workbook
import numpy as np

#REAFING THE XSL WORKBOOK
wb = open_workbook('book_description.xlsx')
#print ((wb.sheets()[0].cell(0,0).value))

#FETCHING THE DESCRIPTION CORRESPONDING TO THE BOOK
def read_discription(b_id):
	for s in wb.sheets():
		content = []
		for row in range(s.nrows):
			col_value = []
			for col in range(s.ncols):
				value  = (s.cell(row,col).value)
				try : value = str(int(value))
				except : pass
				col_value.append(value)
			content.append(col_value)
	
	for i in range(len(content)):
		if content[i][0]==str(b_id):
			return content[i][2]
			break	

#PRINTING THE DESCRIPTION
des=read_discription(92)
print(des)
