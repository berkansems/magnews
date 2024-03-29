from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, redirect

# Create your views here.
from main.decorators import allowed_users
from news.forms import CreateNews
from category.models import Cat
import datetime
@login_required(login_url='my_login')
@allowed_users(allowed_roles = ['admin'])
def cat_list(request):

    cat_list=Cat.objects.all()
    context={'cat_list':cat_list}

    return render(request, 'back/cat_list.html',context)


@login_required(login_url='my_login')
@allowed_users(allowed_roles = ['admin'])
def cat_add(request):

    if request.method=="POST":
        cat=request.POST.get('name')
        print(Cat.objects.filter(name=cat))
        if cat =="":
            print("please input correct category")
            return redirect('cat_add')
        if len(Cat.objects.filter(name=cat)) != 0:
            print("name entered before !!")
            return redirect('cat_add')
        category=Cat(name=cat)
        category.save()
        return redirect('cat_list')
    return render(request, 'back/cat_add.html')


@login_required(login_url='my_login')
@allowed_users(allowed_roles = ['admin'])
def cat_delete(request,pk):

    cat=Cat.objects.get(id=pk)
    cat.delete()
    return redirect('cat_list')