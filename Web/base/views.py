from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.views.generic.base import TemplateView

from django.urls import reverse_lazy
# Create your views here.

class LoginPage(LoginView):
    template_name = 'base/login.html'
    
    def get_success_url(self):
        if self.request.user.userRole == 'EMPLOYEE':
            return reverse_lazy("employee_home")


class TestPage(TemplateView):
    template_name = 'base/index.html'