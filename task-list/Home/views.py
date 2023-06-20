from django.shortcuts import render, redirect
from Home.models import Work

# Create your views here.
def home(request):
    items=Work.objects.all()
    context={
        "items":items
    }
    return render(request,"index.html", context)

def addwork(request):
    return render(request, "add.html")

def stor(request):
    if(request.method == "POST"):
        title=request.POST.get("title")
        description=request.POST.get("description")
        color=request.POST.get("color")
        print("This is teh color "+color)
        entery=Work(title=title, description=description, color=color, complite="False")
        entery.save()
    return redirect("/")

def edit(request, number):
    items=Work.objects.filter(sno = number).first()
    context={
        "item": items
    }
    return render(request, "edit.html", context)
def submitedit(request, number):
    if(request.method == 'POST'):
        entery=Work.objects.filter(sno = number).first()
        title=request.POST.get("title")
        color=request.POST.get("color")
        description=request.POST.get("description")
        entery.title=title
        entery.description=description
        entery.color=color
        entery.save()
    return redirect("/")
def details(request, number):
    details=Work.objects.filter(sno = number).first()
    context={
        "details":details
    }
    return render(request, "details.html", context)

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
    items=Work.objects.filter(color=color)
    context={
        "items":items
    }
    return render(request, "index.html", context)

def checkbox(request, number, datanumber):
    print(number)
    print(datanumber)
    entery=Work.objects.filter(sno = datanumber).first()
    if(number == 1):
        print("Yes this is true")
        entery.complite = "True"
    else:
        entery.complite = "False"
    entery.save()
    return redirect("/")

def delete(request, number):
    data=Work.objects.filter(sno = number).first()
    data.delete()
    return redirect("/")