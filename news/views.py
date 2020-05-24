from django.shortcuts import render

# Create your views here.
from news.models import News


def news_detail(request,pk):
    siteName="MAG | News"
    news= News.objects.get(id=pk)

    context={'siteName':siteName,'news':news}
    return render(request, 'front/news_detail.html', context)