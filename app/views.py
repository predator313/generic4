from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Student
# Create your views here.
class StudentListview(ListView):
    model=Student
    # template_name_suffix='_list'
    #template_name_suffix if we want to change in ours default and make ours some things own custom
    #we also do ordering here
    ordering=['id']
    #if we want to give our own template instead of 
    #default template
    template_name='app/home.html'
    #we also use inbuilt method def __queryset
    #to return the query set filter the query set
    def get_queryset(self):
        return Student.objects.filter(id='2')
    #get_queryset will return the relevent filter amount of the data