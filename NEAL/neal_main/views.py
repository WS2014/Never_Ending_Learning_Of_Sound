import os
import datetime
from django.shortcuts import render
from django.http import HttpResponse
from models import *


def populate():
	object_name = 'Dog'
    	category = 'ANIMAL'
    	url_audio_file = 'link_to_server_file'
    	url = 'source_url'
    	start_time = datetime.datetime.now()
    	end_time = datetime.datetime.now()
    	date_learned = datetime.datetime.now()
    	confidence = 0.3333
    
	NEAL_model.objects.get_or_create(object_name = object_name, category = category, url_audio_file = url_audio_file, url = url, start_time = start_time, end_time = end_time, date_learned = date_learned, confidence = confidence)
	
	
def neal_index(request):
	return render(request, 'neal_main/index.html', {})


def about(request):
	return render(request, 'neal_main/about.html', {})


def downloads(request):
	return render(request, 'neal_main/downloads.html', {})


def objects(request):
	selected_flag = 0==1
	#print 'data insert'
	#os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'NEAL.settings')
	#populate()
	query_results = NEAL_download_model.objects.all()
	category_results = NEAL_download_model.objects.values('category').distinct()
	return render(request, 'neal_main/objects.html', {'query_results': query_results,'selected_flag':selected_flag, 'category_results': category_results, 'selected_category': None, 'object_results': None, 'selected_object': None})

def objects_selected(request, category):
	template = 'neal_main/objects.html'
	selected_flag = 0==0
	os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'NEAL.settings')
	query_results = []
	query_results = NEAL_download_model.objects.filter(category = category)
	category_results = NEAL_download_model.objects.values('category').distinct()
	object_results = NEAL_download_model.objects.filter(category = category).values('object_name').distinct()
	return render(request, 'neal_main/objects.html', {'query_results': query_results,'selected_flag':selected_flag, 'category_results': category_results, 'selected_category': category, 'object_results': object_results, 'selected_object': None})

def category_objects_selected(request, category, object_name):
	template = 'neal_main/objects.html'
	selected_flag = 0==0
	os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'NEAL.settings')
	query_results = []
	query_results = NEAL_download_model.objects.filter(category = category).filter(object_name = object_name)
	category_results = NEAL_download_model.objects.values('category').distinct()
	object_results = NEAL_download_model.objects.filter(category = category).values('object_name').distinct()
	return render(request, 'neal_main/objects.html', {'query_results': query_results,'selected_flag':selected_flag, 'category_results': category_results, 'selected_category': category, 'object_results': object_results, 'selected_object': object_name})



def segments(request):
	print 'data insert'
	os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'NEAL.settings')
	populate()
	query_results = NEAL_download_model.objects.all()
	return render(request, 'neal_main/segments.html', {'query_results': query_results})


# Create your views here. Define templates and try rendering templates from the methods defined here and call these methods from urls.py

