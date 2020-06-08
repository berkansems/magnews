from random import random

from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from category.models import Cat

from contactform.models import Comments
from main.decorators import allowed_users
from main.models import Main
from news.forms import CreateNews
from news.models import News
import datetime

from news.time import timeSet, timeRand
from subCategory.models import SubCategory



def news_detail(request,pk):

    siteName="MAG | News"
    cat=Cat.objects.all()
    subCat = SubCategory.objects.all()

    main = Main.objects.get(id=1)
    news = News.objects.all().order_by('-pk')
    popNews = News.objects.all().order_by('-show')[:3]
    lastNews = News.objects.all().order_by('-pk')[:3]

    ne= News.objects.get(id=pk)
    ne.show=ne.show + 1
    ne.save()


    if request.method == "POST":

        try:
            if request.user.id:
                name = request.user.username
                email = request.user.email
                website = '-'


            else:

                name = request.POST.get('name')
                email = request.POST.get('email')
                website = request.POST.get('website')
                if name == "" or email == "":
                    comments = ne.comments_set.all()
                    counting = comments.count()
                    messages.info(request, 'Error happened! please fill all required fields')
                    context = {'counting': counting, 'siteName': siteName, 'ne': ne, 'cat': cat, 'popNews': popNews,
                               'lastNews': lastNews, 'main': main, 'news': news, 'subCat': subCat}
                    return render(request, 'front/news_comment.html', context)



            txt = request.POST.get('msg')
            print(name, email, website, txt, pk)

            form = Comments(name=name, email=email, website=website, txt=txt, newsId=ne)
            form.save()
            messages.info(request, 'comment successfully sent')

        except:
            messages.info(request, 'Error happened! please try again later..')

    comments = ne.comments_set.all()
    counting = comments.count()
    context={'comments':comments,'counting':counting,'siteName':siteName,'ne':ne,'cat':cat,'popNews':popNews,'lastNews':lastNews, 'main':main, 'news':news,'subCat':subCat}
    return render(request, 'front/news_detail.html', context)

def comment(request,pk):
    siteName = "MAG | News"
    cat = Cat.objects.all()
    subCat = SubCategory.objects.all()
    main = Main.objects.get(id=1)
    news = News.objects.all().order_by('-pk')
    popNews = News.objects.all().order_by('-show')[:3]
    lastNews = News.objects.all().order_by('-pk')[:3]

    ne = News.objects.get(id=pk)


    if request.method == "POST":

        try:
            if request.user.id:
                name = request.user.username
                email = request.user.email
                website = '-'


            else:

                name = request.POST.get('name')
                email = request.POST.get('email')
                website = request.POST.get('website')
                if name == "" or email == "":
                    comments = ne.comments_set.all()
                    counting = comments.count()
                    messages.info(request, 'Error happened! please fill all required fields')
                    context = {'counting': counting, 'siteName': siteName, 'ne': ne, 'cat': cat, 'popNews': popNews,
                               'lastNews': lastNews, 'main': main, 'news': news, 'subCat': subCat}
                    return render(request, 'front/news_comment.html', context)



            txt = request.POST.get('msg')
            print(name, email, website, txt, pk)

            form = Comments(name=name, email=email, website=website, txt=txt, newsId=ne)
            form.save()
            messages.info(request, 'comment successfully sent')

        except:
            messages.info(request, 'Error happened! please try again later..')

    comments = ne.comments_set.all()
    counting = comments.count()

    context = {'comments':comments,'counting': counting, 'siteName': siteName, 'ne': ne, 'cat': cat, 'popNews': popNews,
               'lastNews': lastNews, 'main': main, 'news': news, 'subCat': subCat}
    return render(request, 'front/news_comment.html', context)


@login_required(login_url='my_login')
def news_list(request):
    # check user authenticated or not

    newsList = News.objects.all()
    context={'newsList':newsList}
    return render(request, 'back/news_list.html',context)

@login_required(login_url='my_login')
@allowed_users(allowed_roles = ['admin'])
def add_news(request):
    # check user authenticated or not

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
@login_required(login_url='my_login')
@allowed_users(allowed_roles = ['admin'])
def delete(request,pk):
    # check user authenticated or not
    news=News.objects.get(id=pk)
    
    news.delete()

    return redirect('news_list')

@login_required(login_url='my_login')
def news_edit(request,pk):
    # check user authenticated or not

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
