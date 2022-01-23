from re import template
from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from blogapp.models import Student
from django.urls import reverse_lazy



class StudentCreateView(CreateView):
    model = Student
    fields = ('__all__')
    # queryset = Student.objects.all()
    template_name = 'register/student.html'
    success_url = reverse_lazy('student_list')
    
    
class StudentListView(ListView):
    model = Student
    template_name = 'register/list.html'
    paginate_by = 3
 

class StudentDetailView(DetailView):
    model = Student
    template_name = 'register/detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['student_list'] = Student.objects.all()
        return context
    

class StudentUpdateView(UpdateView):
    model = Student
    fields = ('__all__')
    template_name = 'register/update.html'
    success_url = reverse_lazy('student_list')
    
    
class StudentDeleteView(DeleteView):
    model = Student
    template_name = 'register/delete.html'
    success_url = reverse_lazy('student_list')
    

class Display_allListView(ListView):
    model = Student
    template_name = 'register/display_all.html'
    context_object_name = 'display_all'
    paginate_by  = 5

    
    