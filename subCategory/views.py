from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, redirect

# Create your views here.
from category.models import Cat
from news.forms import CreateNews
from .models import SubCategory
import datetime

def subCategory_list(request):
    # check user authenticated or not
    if not request.user.is_authenticated:
        return redirect('login')
    cat_list=SubCategory.objects.all()
    context={'cat_list':cat_list}

    return render(request, 'back/subCategory_list.html', context)

def subCategory_add(request):
    # check user authenticated or not
    if not request.user.is_authenticated:
        return redirect('login')
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

def subCategory_delete(request,pk):
    # check user authenticated or not
    if not request.user.is_authenticated:
        return redirect('login')
    subcat=SubCategory.objects.get(id=pk)
    subcat.delete()
    return redirect('subCategory_list')


def subCategory_edit(request,pk):
    # check user authenticated or not
    if not request.user.is_authenticated:
        return redirect('login')
    subCat=SubCategory.objects.get(id=pk)
    cat=Cat.objects.all()
    return render(request,'back/subCategory_edit.html',{'subCat':subCat,'cat':cat})