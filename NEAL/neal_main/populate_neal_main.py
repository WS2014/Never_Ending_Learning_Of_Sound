import sqlite3 as lite
import sys
import datetime

def populate():
	conn = lite.connect('./../db.sqlite3')

	with conn:
		cur = conn.cursor()
		#cur.execute("alter table neal_main_neal_download_model modify column id integer auto_increment")
		print "INSERTING"
		with open("static/downloaded_files/downloaded_files.csv", "r") as userfile:
			for line in userfile:
				terms = line.split(",")
				terms = line.split(",")
				terms[0] = terms[0].lower()
				objects = terms[0].split(" ")
				object1 = objects[0]
				#print objects				
				for i in objects:
					if (i!=object1):
						object1 = object1 + "-" + i

				print str(object1)
	
				terms[1] = terms[1].lower()
				category = terms[1].split(" ")
				category1 = category[0]
				for i in category:
					if (i!=category1):
						category1 = category1 + "-" + i
	
				print str(category1)
				#inserting data in the sqlite3 database
				query = "INSERT INTO neal_main_neal_download_model values(NULL, '" + str(object1) + "', '" + str(category1) + "', '" + str(terms[2]) + "', '" + str(terms[3]) + "', '" + str(datetime.datetime.now()) + "');"
				cur.execute(query)
		userfile.close()
		print "INSERTED"



populate()


"""

	




import os
def populate():
	item1 = 'temp1'
	data1 = 'data'
	item2 = 'temp2'
	data2 = 'data2'
	NEAL_model.objects.get_or_create(one=item1, two=data1)
	NEAL_model.objects.get_or_create(one=item2, two=data2)



if __name__ == '__main__':
	print 'data insert'
	os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'NEAL.settings')
	from models import NEAL_model
	populate()

"""
