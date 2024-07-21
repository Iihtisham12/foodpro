from django.shortcuts import render, redirect
from .models import Receipe
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
# Create your views here.


def singUp(request):
    if request.method == "POST":
        r_name = request.POST.get('username')
        r_fname = request.POST.get('first_name')
        r_lname = request.POST.get('last_name')
        r_pass = request.POST.get('password')
        userdata = User(username=r_name, first_name=r_fname, last_name=r_lname )
        userdata.set_password(r_pass)
        userdata.save()

        return redirect('/')
    else:
        pass
    return render(request, 'receipevege/singup.html')


def loginPage(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not User.objects.filter(username=username).exists():
            return redirect('/')
        
        user = authenticate(username=username, password=password)
        if user is None:
            return redirect('/')  
        else:
            login(request, user)
            messages.info(request,'Welcome To DashBoard.')
            return redirect('/receipe/')
           
             
    return render(request, 'receipevege/login.html')


def logoutPage(request):
    logout(request)
    return redirect('/')


@login_required(login_url='/')       #This is Use Only Authenticated User not To Other 
def receipAddeMethod(request):
    if request.method == 'POST':
        data = request.POST
        name = data.get('re_name')
        des = data.get('re_description')
        price = data.get('re_price')
        img = request.FILES.get('re_images')
        user = Receipe(re_name=name,re_description= des,re_price=price, re_images=img)
        user.save()
        data = Receipe()
        # print(f' Name {name} Description {des} Price {price} Image  : {img}')

    else:
        data = Receipe()
    quryset = Receipe.objects.all()

    return render(request,'receipevege/receipe.html',{'form':data,'qdata':quryset})


@login_required(login_url='/')
def updateData(request,id):
    queryset = Receipe.objects.get(id=id)
    if request.POST:
        data = request.POST
        u_name = data.get('re_name')
        u_des = data.get('re_description')
        u_price = data.get('re_price')
        u_img = request.FILES.get('re_images')

        queryset.re_name = u_name
        queryset.re_description = u_des
        queryset.re_price = u_price
        if u_img:
            queryset.re_images = u_img

        queryset.save()
        return redirect('/receipe/')
    return render(request,'receipevege/update.html',{'qdata':queryset})


@login_required(login_url='/')
def deleteData(request,id):
    queryset = Receipe.objects.get(id=id)
    queryset.delete()
    return redirect('/receipe/')
