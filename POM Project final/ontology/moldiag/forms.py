from django import forms
from .models import Diagnosis,HPOEntry

class HPOSelectionForm(forms.Form):
    hpo_entry = forms.ModelChoiceField(queryset=HPOEntry.objects.all(), empty_label=None)

class DiagnosisForm(forms.ModelForm):
    class Meta:
        model = Diagnosis
        fields = ['code', 'description']