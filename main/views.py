from random import random

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

# Create your views here.
from category.models import Cat
from contactform.models import ContactForm
from main.models import Main
from news.models import News
from subCategory.models import SubCategory
from django.contrib.auth import authenticate, login, logout





def home(request):
    siteName="MAG | Home"
    cat=Cat.objects.all()
    subCat=SubCategory.objects.all()


    main=Main.objects.get(id=1)
    news= News.objects.all().order_by('-pk')
    popNews= News.objects.all().order_by('-show')[:3]
    lastNews= News.objects.all().order_by('-pk')[:3]

    context={'siteName':siteName,'main':main ,'news':news,'cat':cat,'subCat':subCat,'lastNews':lastNews,'popNews':popNews}
    return render(request, 'front/home.html',context)

def about(request):
    siteName="MAG | Home"
    main=Main.objects.get(id=1)
    cat = Cat.objects.all()
    subCat = SubCategory.objects.all()

    main = Main.objects.get(id=1)
    news = News.objects.all().order_by('-pk')
    popNews = News.objects.all().order_by('-show')[:3]
    lastNews = News.objects.all().order_by('-pk')[:3]

    context={'siteName':siteName,'main':main ,'news':news,'cat':cat,'subCat':subCat,'lastNews':lastNews,'popNews':popNews}

    return render(request, 'front/about.html',context)


def news(request):
    siteName = "MAG | Home"
    cat = Cat.objects.all()
    subCat = SubCategory.objects.all()

    main = Main.objects.get(id=1)

    lastNews = News.objects.all().order_by('-pk')[:5]
    context = {'siteName': siteName, 'main': main,  'cat': cat, 'subCat': subCat, 'lastNews': lastNews}
    return render(request, 'front/news.html',context)

def category(request):
    siteName = "MAG | Home"
    cat = Cat.objects.all()
    subCat = SubCategory.objects.all()

    main = Main.objects.get(id=1)

    lastNews = News.objects.all().order_by('-pk')[:5]
    context = {'siteName': siteName, 'main': main, 'cat': cat, 'subCat': subCat, 'lastNews': lastNews}

    return render(request,'front/category.html',context)


@login_required(login_url='my_login')
def panel(request):
    #check user authenticated or not
    messages=ContactForm.objects.all()
    count=messages.count()
    xx = 1234455


    return render(request, 'back/home.html',{'count':count,'xx':xx})


def my_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        upass = request.POST.get('password')
        user=authenticate(username=username,password=upass)
        if user != None:
            login(request,user)
            return redirect('panel')


    return render(request, 'front/login.html')

def log_out(request):
    logout(request)
    return redirect('home')

@login_required(login_url='my_login')
def site_setting(request):
    forms=Main.objects.all()
    form=forms[0]
    print(form)

    if request.method == "POST":

        form.name = request.POST.get('title')
        form.about = request.POST.get('about')
        form.facebook = request.POST.get('facebook')
        form.twitter = request.POST.get('twitter')
        form.instagram = request.POST.get('instagram')
        form.save()
        return redirect('panel')

    return render(request,'back/setting.html',{'form':form})

def contact(request):
    siteName = "MAG | Home"
    cat = Cat.objects.all()
    subCat = SubCategory.objects.all()

    main = Main.objects.get(id=1)
    news = News.objects.all().order_by('-pk')
    popNews = News.objects.all().order_by('-show')[:3]
    lastNews = News.objects.all().order_by('-pk')[:3]

    if request.method == "POST":
        try:
            name=request.POST.get('name')
            email=request.POST.get('email')
            website=request.POST.get('website')
            txt=request.POST.get('msg')
            if txt == "" or name == "" or txt == "":
                context = {'siteName': siteName, 'main': main, 'news': news, 'cat': cat, 'subCat': subCat,
                           'lastNews': lastNews,'message': 'please fill all required filds','messageId':'False',
                           'popNews': popNews}
                return render(request, 'front/contact.html', context)
            else:

                message= ContactForm(name=name,email=email,website=website,txt=txt)
                message.save()
                context = {'siteName': siteName, 'main': main, 'news': news, 'cat': cat, 'subCat': subCat,
                           'lastNews': lastNews, 'message': 'Congratulations! Your message successfully sent to us!', 'messageId': 'True',
                           'popNews': popNews}
                return render(request, 'front/contact.html', context)

        except:
            return render(request,'front/contact.html',{'message':'error happened please try later!','messageId':'False'})

    context = {'siteName': siteName, 'main': main, 'news': news, 'cat': cat, 'subCat': subCat, 'lastNews': lastNews,
               'popNews': popNews}

    return render(request,'front/contact.html',context)

@login_required(login_url='my_login')
def message(request):

    message=ContactForm.objects.all()
    count=message.count()
    context={'count':count,'message':message}


    return render(request,'back/message.html',context)

@login_required(login_url='my_login')
def view_message(request,pk):

    message=ContactForm.objects.get(id=pk)

    context={'message':message}


    return render(request,'back/view_message.html',context)
