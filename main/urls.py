from django.urls import path
from . import views


urlpatterns = [
      path("", views.home, name="home") ,#/route
      path("login/",views.login,name="login"),#login rpute
      path("register/",views.register,name="register"),#register route
      path("logout/",views.logout,name="logout"),#logout route
      path("memes/",views.getmemes,name="memes"),#getmemes route
      path("editmeme/",views.editmeme,name="editmemes"), #edit routes
      path("details/",views.memedetails,name="details")
]
      

