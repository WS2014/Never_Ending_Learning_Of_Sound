import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
path = os.path.join(BASE_DIR, 'media/uploaded_class/output.txt')

def get_start_end_times():
	with open(path,"r") as userfile:
		
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

