from django.urls import path
from . import views

urlpatterns = [
    path("", views.signin, name="signin"),
    path("signup", views.signup, name="signup"),
    path("home", views.home, name="home"),
    path("selction", views.selection, name="selection"),
    path("quiz", views.quiz, name="quiz"),
    path("mulquiz", views.mulquiz, name="mulquiz"),
    path("score", views.score, name="score"),
    path("team", views.team, name="team"),
    path("admin-page", views.adminpage, name="admin-page"),




]