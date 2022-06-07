from django import forms

from .models import InfoAdjective, File


class AdjectiveForm(forms.ModelForm):
    class Meta:
        model = InfoAdjective
        fields = "__all__"


class FileForm(forms.ModelForm):
    class Meta:
        model = File
        fields = "__all__"

