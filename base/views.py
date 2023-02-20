from django.shortcuts import render


# Create your views here.

def student_login(request):
    context = {}

    if request.POST:
        print("good stuffs")

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
    context = {}
    return render(request, 'add_new_candidate.html', context)


def view_all_candidates(request):
    context = {}
    return render(request, 'view_all_candidates.html', context)


def view_all_results(request):
    context = {}
    return render(request, 'view_all_results.html', context)


def view_all_students(request):
    context = {}
    return render(request, 'view_all_students.html', context)


def voting_page(request):
    context = {}
    return render(request, 'voting_page.html', context)



