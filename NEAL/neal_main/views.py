import os
import datetime
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from models import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from forms import DocumentForm
from class_read import *

def list_my_files(request):
    # Handle file upload
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            newdoc = Document(docfile = request.FILES['docfile'])
            newdoc.save()

            # Redirect to the document list after POST
            return HttpResponseRedirect(reverse('neal_main:list'))
    else:
        form = DocumentForm() # A empty, unbound form

    # Load documents for the list page
    documents = Document.objects.all()

    # Render list page with the documents and the form
    return render(request, 'neal_main/list.html', {'documents': documents, 'form': form})
    """
    return render_to_response(
        'neal_main/list.html', {'documents': documents, 'form': form}, context_instance=RequestContext(request)
    )
    """

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
	if request.method == 'POST':
        	form = DocumentForm(request.POST, request.FILES)
		if form.is_valid():
        		newdoc = Document(docfile = request.FILES['docfile'])
           		newdoc.save()

            	# Redirect to the document list after POST
            	return HttpResponseRedirect(reverse('neal_main:neal_index'))
    	else:
        	form = DocumentForm() # A empty, unbound form

    	# Load documents for the list page
    	documents = Document.objects.all()
	
	list1 = []
	list1 = get_start_end_times()
		

    	# Render list page with the documents and the form
    	return render(request, 'neal_main/index.html', {'form': form, 'list1':list1})


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

	paginator = Paginator(query_results, 20) # Show 25 contacts per page
	page = request.GET.get('page')
    	try:
        	query_paginated_results = paginator.page(page)
    	except PageNotAnInteger:
        	# If page is not an integer, deliver first page.
        	query_paginated_results = paginator.page(1)
    	except EmptyPage:
        	# If page is out of range (e.g. 9999), deliver last page of results.
        	query_paginated_results = paginator.page(paginator.num_pages)

	return render(request, 'neal_main/objects.html', {'query_results': query_paginated_results,'selected_flag':selected_flag, 'category_results': category_results, 'selected_category': None, 'object_results': None, 'selected_object': None})

def objects_selected(request, category):
	template = 'neal_main/objects.html'
	selected_flag = 0==0
	os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'NEAL.settings')
	query_results = []
	query_results = NEAL_download_model.objects.filter(category = category)
	category_results = NEAL_download_model.objects.values('category').distinct()
	object_results = NEAL_download_model.objects.filter(category = category).values('object_name').distinct()

	paginator = Paginator(query_results, 20) # Show 25 contacts per page
	page = request.GET.get('page')
    	try:
        	query_paginated_results = paginator.page(page)
    	except PageNotAnInteger:
        	# If page is not an integer, deliver first page.
        	query_paginated_results = paginator.page(1)
    	except EmptyPage:
        	# If page is out of range (e.g. 9999), deliver last page of results.
        	query_paginated_results = paginator.page(paginator.num_pages)

		
	return render(request, 'neal_main/objects.html', {'query_results': query_paginated_results,'selected_flag':selected_flag, 'category_results': category_results, 'selected_category': category, 'object_results': object_results, 'selected_object': None})

def category_objects_selected(request, category, object_name):
	template = 'neal_main/objects.html'
	selected_flag = 0==0
	os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'NEAL.settings')
	query_results = []
	query_results = NEAL_download_model.objects.filter(category = category).filter(object_name = object_name)
	category_results = NEAL_download_model.objects.values('category').distinct()
	object_results = NEAL_download_model.objects.filter(category = category).values('object_name').distinct()
	
	paginator = Paginator(query_results, 20) # Show 25 contacts per page
	page = request.GET.get('page')
    	try:
        	query_paginated_results = paginator.page(page)
    	except PageNotAnInteger:
        	# If page is not an integer, deliver first page.
        	query_paginated_results = paginator.page(1)
    	except EmptyPage:
        	# If page is out of range (e.g. 9999), deliver last page of results.
        	query_paginated_results = paginator.page(paginator.num_pages)


	return render(request, 'neal_main/objects.html', {'query_results': query_paginated_results,'selected_flag':selected_flag, 'category_results': category_results, 'selected_category': category, 'object_results': object_results, 'selected_object': object_name})



def segments(request):
	
	os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'NEAL.settings')
	query_results = NEAL_download_model.objects.all()
	return render(request, 'neal_main/segments.html', {'query_results': query_results})


def crawler(request):
	
	os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'NEAL.settings')
	query_results = NEAL_crawl_model.objects.all()
	#youtube_urls = NEAL_crawl_model.objects.values('source_url')
	#print youtube_urls
	#youtube_keys = []
	#for item in youtube_urls:
	#	youtube_keys.append(item['source_url'].split("watch?v=")[1])
	#print youtube_keys
	
	#print query_results
	
	new_query_results = []	

	for item in query_results:
		a = {}
		a['object_name'] = item.object_name
		a['duration'] = item.duration	
		a['keywords'] = item.keywords
		a['date_crawler'] = item.date_crawler
		a['source_url'] = item.source_url
		a['embed_link'] = item.source_url.split("watch?v=")[1]
		new_query_results.append(a)

	paginator = Paginator(new_query_results, 6) # Show 25 contacts per page
	page = request.GET.get('page')
    	try:
        	query_paginated_results = paginator.page(page)
    	except PageNotAnInteger:
        	# If page is not an integer, deliver first page.
        	query_paginated_results = paginator.page(1)
    	except EmptyPage:
        	# If page is out of range (e.g. 9999), deliver last page of results.
        	query_paginated_results = paginator.page(paginator.num_pages)

	return render(request, 'neal_main/crawler.html', {'query_results': query_paginated_results})



# Create your views here. Define templates and try rendering templates from the methods defined here and call these methods from urls.py

