from django.contrib import messages
from django.shortcuts import render, redirect

from app.forms import StudentForm
from app.models import StudentModel
from django.views.generic import FormView

def displayForm(request):
    res=StudentForm()
    return render(request,"One.html",{"form":res})


def insert(request):
    regno=request.POST["S_reg_no"]
    name=request.POST["S_name"]
    email=request.POST["S_email"]
    number=request.POST["S_Number"]
    image=request.POST["S_image"]
    password=request.POST["S_password"]

    StudentModel(regno=regno,name=name,email=email,password=password,image=image,mobile_number=number).save()
    messages.success(request,"Data Inserted Sucessfully")
    return redirect("main")


def login(request):
    email=request.POST["S_email"]
    password = request.POST["S_password"]
    try:
        res=StudentModel.objects.get(email=email,password=password)
    except StudentModel.DoesNotExist:
        messages.success(request, "Details Not Found")
        return redirect("main")
    else:
        return render(request,"welcome.html")


class FormViewDetails(FormView):
    template_name = "two.html"
    form_class = StudentForm


def formview(request):
    re=StudentForm()
    return render(request,"three.html",{"form":re})

def insertform(request):
    regno1=request.POST["regno"]
    name1=request.POST["name"]
    email1=request.POST["email"]
    number1=request.POST["mobile_number"]
    image1=request.POST["image"]
    password1=request.POST["password"]
    gender1 = request.POST["gender"]

    StudentModel(regno=regno1,name=name1,email=email1,password=password1,image=image1,mobile_number=number1,gender=gender1).save()
    messages.success(request,"Data Inserted Sucessfully")
    return redirect("main")