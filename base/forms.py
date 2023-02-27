from django.forms import ModelForm
from .models import Candidate,Voting


class CandidateForm(ModelForm):
    class Meta:
        model = Candidate
        fields = ['name', 'category', 'rank']


class VotingForm(ModelForm):
    class Meta:
        model = Voting
        fields = ['label']

