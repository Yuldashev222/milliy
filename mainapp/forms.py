from django import forms

from .models import InfoAdjective, InfoNoun


class AdjectiveForm(forms.ModelForm):
    class Meta:
        model = InfoAdjective
        fields = "__all__"


class NounForm(forms.ModelForm):
    class Meta:
        model = InfoNoun
        fields = "__all__"