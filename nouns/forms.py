from django import forms

from .models import InfoNoun


class NounForm(forms.ModelForm):
    class Meta:
        model = InfoNoun
        fields = "__all__"