from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Student
# Create your views here.
class StudentListview(ListView):
    model=Student
    # template_name_suffix='_list'
    #template_name_suffix if we want to change in ours default and make ours some things own custom
    #we also do ordering here
    ordering=['name']
