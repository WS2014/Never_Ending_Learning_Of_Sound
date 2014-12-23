import os

def get_start_end_times():
	with open("/home/rohan/Desktop/rohan/Never_Ending_Sound_Learning/NEAL/media/uploaded_class/output.txt","r") as userfile:
		
		class_list = []
		for line in userfile:	
			dictionary = {}
			dictionary['start'] = line.split(":")[0]
			dictionary['end'] = line.split(":")[1].split('\n')[0]
			class_list.append(dictionary)
		
		userfile.close()
	return class_list

list1 = []
list1 = get_start_end_times()
print list1
