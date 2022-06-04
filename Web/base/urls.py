from django.urls import path
from .views import LoginPage, TestPage

urlpatterns = [
    path('', LoginPage.as_view(), name='login'),
    path('test', TestPage.as_view(), name='employee_home')
]