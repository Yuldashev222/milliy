from django import forms

from .models import InfoAdjective


class AdjectiveForm(forms.ModelForm):
    class Meta:
        model = InfoAdjective
        fields = "__all__"

