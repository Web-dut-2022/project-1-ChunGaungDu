from pickle import TRUE
import random
from unittest import result
from django.shortcuts import render

from . import util

import markdown2

from django.core.files.storage import default_storage

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request,entry_name):
    return render(request, "encyclopedia/entry.html",{
        "entry_name" : entry_name,
        "content" : markdown2.markdown(util.get_entry(entry_name))
    })

def search(request):
    entry_name = str( request.GET['q'] )
    title = list()
    flag = 0
    for entry in util.list_entries():
        if entry_name == entry:
            flag = 1
            break
        elif entry_name in entry:
            flag = 2
            title.append(entry)
    if flag == 0:
        return render(request,"encyclopedia/error.html",{"error" : "The page you are looking for does not exist"})
    if flag == 1:
        return render(request,"encyclopedia/entry.html",{"content" : markdown2.markdown(util.get_entry(entry_name)) })
    else:
        return render(request,"encyclopedia/index.html",{"entries" : title})

def randomEn(request):
    entries = util.list_entries()
    count = len(entries)
    num = random.randint(0,count-1)
    title = entries[num]
    return render(request,"encyclopedia/entry.html",{"content" : markdown2.markdown(util.get_entry(title))})


def newEn(request):
    return render(request,'encyclopedia/crepage.html')


def saveNewMD(request):
    title = request.GET['t']
    content = request.GET['c']
    for entries in util.list_entries():
        if title==entries:
            return render(request,'encyclopedia/error.html',{"error" : "This page already exists!"})
    util.save_entry(title,content)
    text = markdown2.markdown(util.get_entry(title))
    return render(request,'encyclopedia/entry.html',{"title " : title ,"content" : text})
