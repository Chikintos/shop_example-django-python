from cProfile import Profile
from re import T
from django.shortcuts import render

import json 
from .models import *
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.detail import SingleObjectMixin
from django import forms
from django.views.generic.edit import FormView
from .forms import UserRegisterForm
from .forms import UserLoginForm
from .forms import UserDataChangeForm, UserPasswordChangeForm
from django.contrib import messages
from django.shortcuts import redirect, render
from django.contrib.auth import login, logout
from .models import Order_In_Wrork, Orders

all_cats = Categories.objects.all()
all_products = Products.objects.all()


def index(request):
    discount=Products.objects.order_by("product_discount")[:4]
    return render(request, "main_shop\index.html", {'title': "Головна сторінка", "Categories": all_cats,"dicountPrd":discount, "Products": all_products})


def UserLogout(request):
    logout(request)
    return redirect('main')


def Settings(request):
    if request.method == "POST":
        form = UserDataChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "Реєстрація відбулась успішно")
            return redirect('login')
        else:
            form = UserDataChangeForm()
            messages.error(request, "Помилка реєстрації")
    form = UserDataChangeForm(instance=request.user)
    return render(request, "main_shop\settings.html", {'title': "Редагування профілю", "Categories": all_cats, "Products": all_products, "form": form})

def multyOrderToJSON(prdid,prdnum,prdname,prdphotopath):
    OrderDict={}
    sendItem={}
    indx=0
    for i in range(1,len(prdid)+1):
        ordItem={}
        ord1Item={}
        ord1Item["productId"]=prdid[indx]
        ord1Item["productNumber"]=prdnum[indx]
        
        ordItem["productId"]=prdid[indx]
        ordItem["productNumber"]=prdnum[indx]
        ordItem["productName"]=prdname[indx]
        ordItem["productPhotoPath"]=prdphotopath[indx]
        OrderDict[i]=ordItem
        sendItem[i]=ord1Item
        indx+=1
    jsonDict=json.dumps(OrderDict, indent = 4, ensure_ascii=False) 

    return [OrderDict,sendItem]
def aboutUs(request):
    return render(request, "main_shop/aboutus.html", {'title': "Про нас", "Categories": all_cats, "Products": all_products})
    pass
def clearBasket(request):
    username=request.user 
    Basketdel = Orders.objects.filter(user_id = username)
    Basketdel.delete()
    return redirect('basket')

def OrderPage(request, id=0, num=0):
    if id == 0 and num==0:
        prdid = request.POST['prdId'].split(",")
        prdnum= request.POST['prdnum'].split(",")
        prdname=request.POST['prdName'].split(",")
        
        prdphotopath=request.POST['product_img_path'].split(",")
        prdphotopath=prdphotopath[::2]
        Multyreturn=multyOrderToJSON(prdid,prdnum,prdname,prdphotopath)
        JsonDict=Multyreturn[0]
        sendDict=Multyreturn[1]
        x=2
        return render(request, "main_shop\order_page.html", {'title': "Оформлення замовлення", "Categories": all_cats,"multyOrder":JsonDict ,"Products": all_products,"SendDict":sendDict,"number": num,"x":x})
    else:
        OrderProduct = Products.objects.get(pk=id)
        x=1
        return render(request, "main_shop\order_page.html", {'title': "Оформлення замовлення", "Categories": all_cats, "Products": all_products, "ProdInOrder": OrderProduct, "number": num,"x":x})


def orderInfoJSON(id, num):
    order = {}
    order[1] = {"prod_id": id, "num_of_prod": num}
    return order


def saveorder(request):
    order = Order_In_Wrork()
    if request.POST['NumOfProduct']=="0":
        order.order_info = request.POST['orderInfo']
    else:
        order.order_info = orderInfoJSON(
        request.POST['itemId'], request.POST['NumOfProduct'])
    order.user_id = request.POST['username']
    order.ord_surname = request.POST['surname']
    order.phone_number = request.POST['phone_number']
    order.adress = request.POST['index']
    order.additional_info = request.POST['comments']
    order.ord_name = request.POST['ownname']
    order.save()

    return render(request, "main_shop/index.html", {'title': 'Сторінка товару', "Categories": all_cats, "Products": all_products, "product": product})


def addtobasket(request, id, num, user):
    order = Orders()

    productInitial=str(Products.objects.filter(pk=id).values("product_price_initial")).replace("<QuerySet [{'product_price_initial': Decimal('", '').replace("')}]>", '')
    productDiscount=str(Products.objects.filter(pk=id).values("product_discount")).replace("<QuerySet [{'product_discount': Decimal('", '').replace("')}]>", '')
    print(productInitial)
    print(productDiscount)
    a=float(productInitial)-float(productInitial)/100*float(productDiscount)
    
    order.user_id = user
    order.product_id = id
    order.num_of_products=float(num)
    order.product_name = str(Products.objects.filter(pk=id).values("product_name")).replace("<QuerySet [{'product_name': '", '').replace("'}]>", '')
    order.product_png = str(Products.objects.filter(pk=id).values("product_png")).replace("<QuerySet [{'product_png': '", '').replace("'}]>", '').replace(' ',"")
    order.product_final_price=(float(productInitial)-(float(productInitial)/100*float(productDiscount)))*num
    order.save()
    print(id)
    return redirect('/product/'+str(id))


def changepassword(request):
    if request.method == "POST":
        form = UserPasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()

            messages.success(request, "Успішно")
            return redirect('main')
        else:
            messages.error(request, "Помилка")
            return redirect('passwordchange')
    else:
        form = UserPasswordChangeForm(user=request.user)

        return render(request, "main_shop\passchange.html", {'title': "Редагування паролю", "Categories": all_cats, "Products": all_products, "form": form})


def registrPanel(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Реєстрація відбулась успішно")
            return redirect('login')
        else:
            form = UserRegisterForm()
            messages.error(request, "Помилка реєстрації")
    else:
        form = UserRegisterForm()

    return render(request, "main_shop/register.html", {'title': 'Регистрація', "Categories": all_cats, "Products": all_products, 'form': form})


def LoginPanel(request):
    if request.method == "POST":
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)

            return redirect('main')
        else:
            form = UserLoginForm()
            messages.error(request, "Помилка авторизації")
    else:
        form = UserLoginForm()
    return render(request, "main_shop/login.html", {'title': 'Авторизація', "Categories": all_cats, "Products": all_products, 'form': form})

# Create your views here.


def ProductPage(request, id):
    product = Products.objects.get(pk=id)
    return render(request, "main_shop/product_page.html", {'title': 'Сторінка товару', "Categories": all_cats, "Products": all_products, "product": product})


def basket(request):
    username = request.user
    ordDb = Orders.objects.filter(user_id=username).values()

    ord = ordDb
    return render(request, "main_shop/basket.html", {'title': 'Кошик', "Categories": all_cats, "Products": all_products, "basketProd": ord})

    print('=================')

def category(request,id):
    query_cat=Products.objects.filter(Category_name=id)
    catname=query_cat[1].Category_name
    return render(request, "main_shop/category.html", {'title': 'Товари категорії: '+str(catname),"Categories": all_cats, "Category": query_cat, "Products": all_products, "basketProd": ord})