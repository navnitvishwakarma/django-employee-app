from django.shortcuts import render
from employee.models import Employee

def home(request):
    return render(request, 'home.html')

def blog(request):
    return render(request, 'blog.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')
# def bloghome(request):
#     return render(request, 'bloghome.html')

def htsc(request):
    return render(request, 'htsc.html')
def bloghome(request):
    emp = Employee.objects.all()
    
    context = {
       'employee' : emp,
    }
    return render(request, 'bloghome.html', context)