from django.http.response import HttpResponse
from django.shortcuts import render,HttpResponse
from . models import Register

# Create your views here.

def index(request):
    return render(request,'index.html')

def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        x=Register.objects.get(Email=email)
        if(x.Email == email and x.Password == password):

            return render(request,'loged.html')
    return render(request,'login.html')

def register(request):
    return render(request,'register.html')

def user_register(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        mobile = request.POST['mobile']
        gender = request.POST['gender']
        city = request.POST['city']
        password = request.POST['password']

        x=Register.objects.create(Name=name,Email=email,Mobile=mobile,Gender=gender,City=city,Password=password)
        x.save()
        print("Data Inserted Successfully")
        return render(request,'register.html')
    
