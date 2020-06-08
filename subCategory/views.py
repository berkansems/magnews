from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, redirect

# Create your views here.
from category.models import Cat
from main.decorators import allowed_users
from news.forms import CreateNews
from .models import SubCategory
import datetime
@login_required(login_url='my_login')
@allowed_users(allowed_roles = ['admin'])
def subCategory_list(request):

    cat_list=SubCategory.objects.all()
    context={'cat_list':cat_list}

    return render(request, 'back/subCategory_list.html', context)

@login_required(login_url='my_login')
@allowed_users(allowed_roles = ['admin'])
def subCategory_add(request):

    cat=Cat.objects.all()

    if request.method=="POST":
        subCategoryName=request.POST.get('name')
        subCategoryCat=request.POST.get('subcat')
        categoryName=Cat.objects.get(id=subCategoryCat).name

        if subCategoryName =="":
            print("please input correct category")
            return redirect('subCategory_add')
        if len(SubCategory.objects.filter(name=subCategoryName)) != 0:
            print("name entered before !!")
            return redirect('subCategory_add')
        subCategory=SubCategory(name=subCategoryName,catId=subCategoryCat, catName=categoryName)

        subCategory.save()
        return redirect('subCategory_list')
    return render(request, 'back/subcategory_add.html',{'cat':cat})

@login_required(login_url='my_login')
@allowed_users(allowed_roles = ['admin'])
def subCategory_delete(request,pk):

    subcat=SubCategory.objects.get(id=pk)
    subcat.delete()
    return redirect('subCategory_list')

@login_required(login_url='my_login')
def subCategory_edit(request,pk):

    subCat=SubCategory.objects.get(id=pk)
    cat=Cat.objects.all()
    return render(request,'back/subCategory_edit.html',{'subCat':subCat,'cat':cat})