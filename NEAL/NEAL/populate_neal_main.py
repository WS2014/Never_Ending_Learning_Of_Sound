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
