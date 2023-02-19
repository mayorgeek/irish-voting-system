from django.shortcuts import render


# Create your views here.

def student_login(request):
    context = {}
    return render(request, 'student_login.html', context)


def student_register(request):
    context = {}
    return render(request, 'student_register.html', context)


def admin_login(request):
    context = {}
    return render(request, 'admin_login.html', context)


def admin_register(request):
    context = {}
    return render(request, 'admin_register.html', context)

