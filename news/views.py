from random import random

from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, redirect

# Create your views here.
from category.models import Cat
from news.forms import CreateNews
from news.models import News
import datetime

from news.time import timeSet, timeRand


def news_detail(request,pk):

    siteName="MAG | News"
    cat=Cat.objects.all()
    ne= News.objects.get(id=pk)
    ne.show=ne.show + 1
    ne.save()

    context={'siteName':siteName,'ne':ne,'cat':cat}
    return render(request, 'front/news_detail.html', context)


def news_list(request):
    # check user authenticated or not
    if not request.user.is_authenticated:
        return redirect('my_login')
    newsList = News.objects.all()
    context={'newsList':newsList}
    return render(request, 'back/news_list.html',context)


def add_news(request):
    # check user authenticated or not
    if not request.user.is_authenticated:
        return redirect('my_login')
    news=News.objects.all()
    cat=Cat.objects.all()


    if request.method=="POST":
        timeset = timeSet()
        timerand= timeRand()
        newsTitle=request.POST.get("newstitle")
        newscat=request.POST.get("newscat")
        newstextshort = request.POST.get("newstextshort")
        bodyText = request.POST.get("bodyText")
        mydoc=request.FILES["mydoc"]

        fs=FileSystemStorage()
        fs.save(mydoc.name,mydoc)

        if  newsTitle=="":
            context = {'error': 'fill all sections'}
            return render(request,'back/error.html', context)
        else:
            try:

                newNews=News(id=timerand,short_text=newstextshort,body_text=bodyText,category=newscat,name=newsTitle,pic=mydoc,date=timeset,rand=timerand)
                newNews.save()
                return redirect('news_list')
            except:
                context={'error':'image not selected'}
                return render(request,'back/error.html', context)

    context={'news':news,'cat':cat}
    return render(request, 'back/news_add.html',context)

def error(request):
    return render(request,'back/error.html')

def delete(request,pk):
    # check user authenticated or not
    if not request.user.is_authenticated:
        return redirect('my_login')

    news=News.objects.get(id=pk)
    
    news.delete()

    return redirect('news_list')

def news_edit(request,pk):
    # check user authenticated or not
    if not request.user.is_authenticated:
        return redirect('my_login')

    news=News.objects.get(id=pk)
    if request.method=="POST":
        timeset=timeSet()
        newsTitle = request.POST.get("newstitle")
        newscat = request.POST.get("newscat")
        newstextshort = request.POST.get("newstextshort")
        bodyText = request.POST.get("bodyText")
        mydoc = request.FILES["mydoc"]

        newNews = News(id=pk, date=timeset ,short_text=newstextshort, body_text=bodyText, category=newscat, name=newsTitle, pic=mydoc)

        newNews.save()
        return redirect('news_list')
    return render(request,'back/news_edit.html',{'news':news})
