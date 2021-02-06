from dango.forms import ModelForm
from .models import *

class ApplyForm(ModelForm):
    class Meta:
        model=Candidates
        fieds="__all__"