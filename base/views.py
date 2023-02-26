from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from .forms import CandidateForm
from .models import Candidate


# Create your views here.

def student_login(request):

    if request.user.is_authenticated:
        return redirect('account_page')

    if request.method == 'POST':
        student_id = request.POST.get('student_id')
        password = request.POST.get('password')

        # try:
        #     student = Student.objects.get(student_id=student_id)
        # except:
        #     messages.error(request, "Student does not exist")

        student = authenticate(request, email=student_id, password=password)

        if student is None:
            login(request, student)
            return redirect('account_page')
        else:
            messages.error(request, "Invalid Username or Password")

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


def account_page(request):
    context = {}
    return render(request, 'account_page.html', context)


def start_voting(request):

    context = {}
    return render(request, 'start_voting.html', context)


def view_all_voting(request):
    context = {}
    return render(request, 'view_all_voting.html', context)


def add_new_candidate(request):

    candidates = Candidate.objects.filter(rank=request.POST.get("rank"))

    if request.method == 'POST':
        if candidates.count() > 0:
            messages.error(request, "This Rank is Already Taken!")
        else:
            form = CandidateForm(request.POST)
            form.save()
            if form.is_valid():
                form.save()
                return redirect('view_all_candidates')

    context = {}
    return render(request, 'add_new_candidate.html', context)


def view_all_candidates(request):

    candidates = Candidate.objects.all()

    context = {'candidates': candidates}
    return render(request, 'view_all_candidates.html', context)


def remove_candidate(request, pk):

    candidate = Candidate.objects.get(id=pk)

    if request.method == 'POST':
        candidate.delete()
        return redirect('view_all_candidates')

    return render(request, 'remove_candidate.html')


def view_all_results(request):
    context = {}
    return render(request, 'view_all_results.html', context)


def view_all_students(request):
    context = {}
    return render(request, 'view_all_students.html', context)


def voting_page(request):

    labels =

    context = {}
    return render(request, 'voting_page.html', context)



