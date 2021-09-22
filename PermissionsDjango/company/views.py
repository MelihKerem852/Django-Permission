from django.shortcuts import redirect, render
from django.views.generic import ListView,TemplateView,CreateView,DetailView,UpdateView,DeleteView
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.views import redirect_to_login
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from .models import Company

# Create your views here.

class UserAccessMixin(PermissionRequiredMixin):
    def dispatch(self,request,*args,**kwargs):
        if not self.request.user.is_authenticated:
            return redirect_to_login(self.request.get_full_path(),
                                     self.get_login_url(),self.get_redirect_field_name())
        if not self.has_permission():
            return redirect('/company/list')
        return super(UserAccessMixin,self).dispatch(request,*args,**kwargs)

class CompanyList(ListView):
    model = Company    
    context_object_name= 'companies'
    template_name="index.html"


class AddCompany(UserAccessMixin,CreateView):
    
    raise_exception = False
    permission_required = 'company.add_company'
    permission_denied_message = ""
    login_url = '/company/list/'
    redirect_field_name = 'next'

    template_name = 'create_company.html'
    model = Company
    fields = '__all__'
    success_url = reverse_lazy('company_list')

class CompanyDetail(DetailView):
    model= Company
    context_object_name="company"
    template_name = 'company_detail.html'


class CompanyUpdate(UserAccessMixin,UpdateView):

    raise_exception = False
    permission_required = 'edit.add_company'
    permission_denied_message = ""
    login_url = '/company/list/'
    redirect_field_name = 'next'

    model= Company
    fields = '__all__'
    template_name = "create_company.html"
    success_url = reverse_lazy('company_list')


class CompanyDelete(UserAccessMixin,DeleteView):

    raise_exception = False
    permission_required = 'company.delete_company'
    permission_denied_message = ""
    login_url = '/company/list/'
    redirect_field_name = 'next'

    template_name = 'company_confirm_delete.html'
    model = Company
    context_object_name = 'company'
    success_url = reverse_lazy('company_list')
