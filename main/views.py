from django.shortcuts import render

# Create your views here.
from main.models import Main
from news.models import News


def home(request):
    siteName="MAG | Home"
    main=Main.objects.get(id=1)
    news= News.objects.all()

    context={'siteName':siteName,'main':main ,'news':news}
    return render(request, 'front/home.html',context)

def about(request):
    siteName="MAG | Home"
    main=Main.objects.get(id=1)

    context={'siteName':siteName,'main':main }

    return render(request, 'front/about.html',context)


def news(request):
    return render(request, 'front/news_detail.html')

def category(request):
    return render(request,'front/category.html')


def panel(request):
    return render(request, 'back/home.html')