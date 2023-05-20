from django import forms
from.models import Research


class AddResearch(forms.ModelForm):
    class Meta:
        model = Research
        fields = "__all__"
