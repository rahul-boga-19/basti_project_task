from django.shortcuts import render, redirect
from .models import Applicant

def home(request):
    return render(request, 'home.html')

def register(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        mobile = request.POST['mobile']
        role = request.POST['role']
        message = request.POST['message']

        Applicant.objects.create(name=name, email=email, mobile=mobile, role=role, message=message)
        return redirect('home')

    return render(request, 'register.html')

def admin_view(request):
    applicants = Applicant.objects.all()
    return render(request, 'admin_view.html', {'applicants': applicants})
