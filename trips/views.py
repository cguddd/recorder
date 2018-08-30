# trips/views.py

from datetime import datetime
from flask import request
from django.shortcuts import render, redirect
from trips.forms import DocumentForm
from django.db import models
from trips.models import Document
from django.http import HttpResponse
from django.utils.html import escape
import datetime
import json

ctx = {}
rlt = ""
#words = ['一','二','三','四','五','六','七','八','九','十','後退','前進','上','下','左','右','床','去','快樂','房屋','樹','鳥','貓','狗','志明','春嬌','可以','不可','開','關']
#ctx['th'] = 0
word = ""
ctx['word'] = "一"

def recorder(request):
    return render(request, 'recorder.html', {
    })

def set_name(request):
    return render(request, 'set_name.html', {
    })

def model_form_upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect('/upload')
    else:
        form = DocumentForm()
    return render(request, 'model_form_upload.html', {
        'form': form
    })

def upload_word(request):
    ctx['word'] = request.POST.get('thisword')
    return HttpResponse(escape(repr(request)))

def upload(request):
    customHeader = request.META['HTTP_MYCUSTOMHEADER']

    time = "documents/" + ctx['word']  + "/" + ctx['word']  + "_" + ctx['rlt'] + "_" + datetime.datetime.now().strftime("%Y%m%d_%H%M%S.%f")[:-3] + ".wav"
    # obviously handle correct naming of the file and place it somewhere like media/uploads/
    uploadedFile = open(time, "wb")
    # the actual file is in request.body
    uploadedFile.write(request.body)
    uploadedFile.close()
    # put additional logic like creating a model instance or something like this here
    return HttpResponse(escape(repr(request)))

def name_post(request):
    if request.POST:
        ctx['rlt'] = request.POST['q']
        if(ctx['rlt'] == ""):
            ctx['rlt'] = "user" + datetime.datetime.now().strftime("%f")[:-3]
        return render(request, "recorder.html", ctx)
    else:
        ctx['rlt'] = ""
        return render(request, "set_name.html")