from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from .forms import CandidateForm,VotingForm
from .models import Candidate,Voting,User,Vote


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

    if request.method == 'POST':
        form = VotingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view_all_voting')

    context = {}
    return render(request, 'start_voting.html', context)


def view_all_voting(request):

    votings = Voting.objects.all()

    context = {'votings': votings}
    return render(request, 'view_all_voting.html', context)


def add_new_candidate(request):

    candidates = Candidate.objects.filter(rank=request.POST.get("rank"))

    if request.method == 'POST':
        if candidates.count() > 0:
            messages.error(request, "This Rank is Already Taken!")
        else:
            form = CandidateForm(request.POST)
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

    voting_labels = Voting.objects.all()
    results = []

    for voting in voting_labels:
        candidates = Candidate.objects.filter(category=voting.label)

        first_candidate = ""
        second_candidate = ""
        third_candidate = ""
        fourth_candidate = ""

        first_candidate_votes = 0
        second_candidate_votes = 0
        third_candidate_votes = 0
        fourth_candidate_votes = 0

        try:
            first_candidate = candidates[0]
            first_candidate_votes = Vote.objects.filter(preferred_candidate=candidates[0].name).count()
        except:
            messages.error(request, "No first candidate vote yet")

        try:
            second_candidate = candidates[1]
            second_candidate_votes = Vote.objects.filter(preferred_candidate=candidates[1].name).count()
        except:
            messages.error(request, "No second candidate vote yet")

        try:
            third_candidate = candidates[2]
            third_candidate_votes = Vote.objects.filter(preferred_candidate=candidates[2].name).count()
        except:
            messages.error(request, "No third candidate vote yet")

        try:
            fourth_candidate = candidates[3]
            fourth_candidate_votes = Vote.objects.filter(preferred_candidate=candidates[3].name).count()
        except:
            messages.error(request, "No fourth candidate vote yet")

        data = {
            'label': voting.label,
            'candidates': candidates,
            'first_candidate': first_candidate,
            'second_candidate': second_candidate,
            'third_candidate': third_candidate,
            'fourth_candidate': fourth_candidate,
            'first_candidate_votes': first_candidate_votes,
            'second_candidate_votes': second_candidate_votes,
            'third_candidate_votes': third_candidate_votes,
            'fourth_candidate_votes': fourth_candidate_votes,
        }

        results.append(data)

    context = {'results': results}

    return render(request, 'view_all_results.html', context)


def view_all_students(request):

    users = User.objects.get(role="student")

    context = {'users': users}
    return render(request, 'view_all_students.html', context)


def voting_page(request):

    candidates = Candidate.objects.all()
    categories = Voting.objects.all()

    context = {'candidates': candidates, 'categories': categories}
    return render(request, 'voting_page.html', context)



