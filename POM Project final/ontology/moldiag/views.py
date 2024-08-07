from django.shortcuts import render,HttpResponse, redirect
from .models import HPOEntry, Diagnosis
from .forms import HPOSelectionForm, DiagnosisForm
# Create your views here.

def home(request):
    return render(request,"index.html")

def select_hpo_entries(request):
    if request.method == 'POST':
        form = HPOSelectionForm(request.POST)
        if form.is_valid():
            # Process form data
            hpo_entry = form.cleaned_data['hpo_entry']
            # Additional logic here
    else:
        form = HPOSelectionForm()
    return render(request, 'ontology/select_hpo_entries.html', {'form': form})

def group_hpo_entries(request):
    # Logic for grouping HPO entries
    return render(request, 'ontology/group_hpo_entries.html', context={})

def translate_results(request):
    # Logic for translating results
    return render(request, 'ontology/translate_results.html', context={})