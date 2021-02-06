from django.forms import ModelForm
from .models import Candidates

class ApplyForm(ModelForm):
    class Meta:
        model=Candidates
        fieds="__all__"