from django.shortcuts import render, redirect

# Create your views here.
from contactform.models import ContactForm


def contact_add(request):

    if request.method =="POST":
        try:
            name=request.POST.get('name')
            email=request.POST.get('email')
            website=request.POST.get('website')
            txt=request.POST.get('msg')
            if txt == "" or name == "" or txt == "":
                return render(request, 'front/msgbox.html', {'message': 'please fill all required filds','messageId':'1'})
            else:

                message= ContactForm(name=name,email=email,website=website,txt=txt)
                message.save()
                return render(request, 'front/msgbox.html', {'message': 'message sent successfully','messageId':'2'})
        except:
            return render(request,'front/msgbox.html',{'message':'error happened please try later!','messageId':'2'})

    return render(request,'front/msgbox.html')