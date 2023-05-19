from django.shortcuts import render
from .models import signup
# Create your views here.
def home(request):
    if request.method == 'POST':
        fullName = request.POST['full_name']
        emailId = request.POST['email']
        password = request.POST['password']
        confirmPassword = request.POST['confirm_password']
        phone = request.POST['phone']
        # print(fullName,emailId,password,phone,confirmPassword)
        data = signup(name=fullName,email=emailId,password=password,phone=phone)
        data.save()
        print(data)
    return render(request,'home.html')