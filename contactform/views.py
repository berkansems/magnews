from django.shortcuts import render, redirect

# Create your views here.
from category.models import Cat

from contactform.models import ContactForm
from main.models import Main
from news.models import News
from subCategory.models import SubCategory
from django.contrib import messages


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
            if request.user == None:
                name=request.POST.get('name')
                email=request.POST.get('email')
                website=request.POST.get('website')
                txt=request.POST.get('msg')
                if txt == "" or name == "" or email == "":
                    messages.info(request,'Name, email or text message fields should not be empty!')

            else:
                name=request.user.username
                email=request.user.email
                website=request.user.email
                txt=request.POST.get('msg')
                if txt == "":
                    messages.info(request, 'Text message field should not be empty!')


            message= ContactForm(name=name,email=email,website=website,txt=txt)
            message.save()
            messages.info(request, 'Your message successfully sent!')

        except:
            return render(request,'front/contact.html',{'message':'error happened please try later!','messageId':'False'})

    context = {'siteName': siteName, 'main': main, 'news': news, 'cat': cat, 'subCat': subCat, 'lastNews': lastNews,
               'popNews': popNews}

    return render(request,'front/contact.html',context)


