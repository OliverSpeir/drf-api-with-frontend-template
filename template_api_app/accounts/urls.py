# lines 2 - 8 added in template
from django.urls import path
from django.contrib.auth import views
from .views import CreateAccountView
from .forms import UserLoginForm

urlpatterns = [
    path("create_account/", CreateAccountView.as_view(), name="create_account"),
    path('login/', views.LoginView.as_view(template_name="registration/login.html", authentication_form=UserLoginForm), name='login')
]
