from django.urls import path
from . import views


urlpatterns = [
      path("", views.home, name="home") ,#/route
      path("login/",views.login,name="login"),#login rpute
      path("register/",views.register,name="register")#register route
]
      

