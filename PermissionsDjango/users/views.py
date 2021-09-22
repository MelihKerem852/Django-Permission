from django.shortcuts import redirect, render
from django.contrib.auth.views import LoginView,LogoutView
from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.urls import reverse_lazy

# Create your views here.
class CustomLoginView(LoginView):
    template_name = 'login.html'
    fields= '__all__'
    redirect_authenticated_user = True
    def get_success_url(self):
        return reverse_lazy('company_list')
    

class RegisterPage(FormView):
    template_name = 'register.html'
    from_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('company_list')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterPage,self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('company_list')
        return super(RegisterPage,self).get(*args,**kwargs) 