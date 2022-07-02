# from django.http import HttpResponse
# from django.shortcuts import render


from importlib.resources import path
from django.forms import ImageField
from django.shortcuts import render
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
from requests import request
from h5_model import *

from fresh_fruit.model import detection
from fresh_fruit import settings
import os
# from django.http import HttpResponseRedirect



def index(request):
    return render(request, 'index.html')




file_list = []
def live(request):
    url_list = []
    res_value = ""
    
    if request.method == 'POST':
        files = request.FILES.getlist('files')
        for file in files:

            fs = FileSystemStorage()
            name =fs.save(file.name, file)

            url_file = fs.url(name)
            url_list.append(url_file)


            path_var = f"media/{name}"
            file_list.append(path_var)

        res_value = detection(file_list)
    return render(request,'live.html',{'url':url_list,'dis_url':res_value})



def detected_images(request):
    path = "media"
    img_list = os.listdir(path)
    context = {"images": img_list}  
    return render (request, 'detected_images.html', context)

