from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from Home.models import Work
from django.contrib.auth.models import User
import datetime
import pytz
from django.contrib.auth.hashers import *
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
# Create your views here.
def home(request):
    context={}
    if(request.user.is_authenticated):
        items=Work.objects.filter(email = request.user.email).all()
        name=request.user.email
        context={
            "items":items,
            "name":name.split("@")[0],
            "number":"",
            "gretting": gretting(),
        }
    return render(request,"index.html", context)
@login_required(login_url="/login/")
def addwork(request):
    return render(request, "add.html")
@login_required(login_url="/login/")
def stor(request):
    if(request.method == "POST"):
        title=request.POST.get("title")
        description=request.POST.get("description")
        color=request.POST.get("color")
        print("This is teh color "+color)
        entery=Work(email = request.user.email, title=title, description=description, color=color, complite="False")
        entery.save()
    return redirect("/")

@login_required(login_url="/login/")
def edit(request, number):
    items=Work.objects.filter(sno = number).first()
    context={
        "item": items
    }
    print(context["item"].color)

    return render(request, "edit.html", context)

@login_required(login_url="/login/")
def submitedit(request, number):
    if(request.method == 'POST'):
        entery=Work.objects.filter(sno = number).first()
        title=request.POST.get("title")
        color=request.POST.get("color")
        print(color)
        description=request.POST.get("description")
        entery.title=title
        entery.description=description
        entery.color=color
        entery.save()
    return redirect("/")

@login_required(login_url="/login/")
def details(request, number):
    details=Work.objects.filter(sno = number).first()
    context={
        "details":details
    }
    return render(request, "details.html", context)

@login_required(login_url="/login/")
def addcolor(request, number, colornumber):
    entery=Work.objects.filter(sno=number).first()
    if(colornumber == 1):
        entery.color="rgb(164, 236, 211)"
    elif(colornumber == 2):
        entery.color="rgb(249, 189, 219)"
    elif(colornumber == 3):
        entery.color="rgb(194, 185, 255)"
    else:
        entery.color="rgb(255, 249, 221)"
    entery.save()
    return redirect("/")

@login_required(login_url="/login/")
def selectedColor(request, number):
    color=""
    if(number == 1):
        color="rgb(164, 236, 211)"
    elif(number == 2):
        color="rgb(249, 189, 219)"
    elif(number == 3):
        color="rgb(194, 185, 255)"
    else:
        color="rgb(255, 249, 221)"
    items=Work.objects.filter(color=color, email=request.user.email).all()
    context={
        "items":items,
        "number": number,
    }
    return render(request, "index.html", context)

@login_required(login_url="/login/")
def checkbox(request, number, datanumber):
    print(number)
    print(datanumber)
    entery=Work.objects.filter(sno = datanumber).first()
    if(number == 1):
        entery.complite = "True"
    else:
        entery.complite = "False"
    entery.save()
    return redirect("/")

@login_required(login_url="/login/")
def delete(request, number):
    data=Work.objects.filter(sno = number).first()
    data.delete()
    return redirect("/")


def login_page(request):
    if(request.method == "POST"):
        email=request.POST.get("email")
        password=request.POST.get("password")
        user=User.objects.filter(email = email).first()
        if(user == None):
            messages.warning(request, "User Not Found")
            return redirect("/login/")
        if(not check_password(password, user.password)):
            messages.warning(request, "Password Incorect")
            return redirect("/login/")
        else:
            login(request, user)
            return redirect("/")
    return render(request, "login.html")

def register(request):
    if(request.method == "POST"):
        email=request.POST.get("email")
        password=request.POST.get("password")
        repassword=request.POST.get("repassword")
        data=User.objects.filter(email = email).first()
        if(data != None):
            messages.warning(request, "User alrady Exists ")
            return redirect("/register/")
        elif(password != repassword):
            messages.warning(request, "Password and Repassword is not same ")
            return redirect("/register/")
        else:
            print(make_password(password))
            entery=User(email = email)
            entery.set_password(password)
            entery.save()
            return redirect("/login/")
    return render(request, "register.html")

@login_required(login_url="/login/")
def logout_user(request):
    logout(request)
    return redirect("/")

def gretting():
    time_utc = datetime.datetime.now(pytz.UTC)

    # Convert the time to Indian Standard Time (IST)
    indian_timezone = pytz.timezone('Asia/Kolkata')
    time = time_utc.astimezone(indian_timezone)
    hours=time.strftime("%I")  # This hours
    fo=time.strftime("%p")   # This is PM, AM
    if(5 <= int(hours) and int(hours) <= 11 and fo == "AM"):
        return "Morning"
    elif(12 == int(hours) and fo == "PM" or 1 <= int(hours) and int(hours) <= 5 and fo == "PM"):
        return "Afternoon"
    elif(6 <= int(hours) and int(hours) < 11 and fo == "PM"):
        return "Evening"
    elif 11 <= int(hours) and int(hours) < 12 and fo == "PM" or int(hours) == 12 and fo == "AM" or 1 <= int(hours) and 4 >= int(hours) and fo == "AM":
        return "Night"