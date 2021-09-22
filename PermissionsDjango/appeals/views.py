from django.shortcuts import render
from django.views.generic.edit import DeleteView, UpdateView
from .models import Appeal
from django.views.generic import ListView,TemplateView,CreateView,DetailView
from django.urls import reverse_lazy
# Create your views here.

class AppealList(ListView):
    model = Appeal
    context_object_name = 'appeals'
    template_name = 'appeals/appeal_list.html'

class AddApeal(CreateView):
    template_name = 'appeals/appeal_form.html'
    model = Appeal
    fields = '__all__'
    success_url = reverse_lazy('company_list')


class AppealDetail(DetailView):
    model= Appeal
    context_object_name="appeal"
    template_name = 'appeals/appeal_detail.html'


class UpdateAppeal(UpdateView):
    template_name = 'appeals/appeal_form.html'
    model = Appeal
    fields = '__all__'
    success_url = reverse_lazy('company_list')

class DeleteAppeal(DeleteView):
    model = Appeal
    context_object_name = 'appeals'
    success_url = reverse_lazy('company_list')




