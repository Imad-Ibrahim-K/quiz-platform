from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from .models import UserProfile


# Create your views here.
def signin(request):


    return render(request, "index.html")


def signup(request):
    if request.method == "POST":
        fullName = request.POST.get("fullName")
        userName = request.POST.get("userName")
        password = request.POST.get("pass")
        password2 = request.POST.get("passCon")
        emailId = request.POST.get("emailId")

        # Validate the password
        # try:
        #     validate_password(password)
        # except ValidationError as e:
        #     # The password is not valid, return the error messages
        #     return render(request, "registration_page.html", {"errors": e.messages})

        # Check if the passwords match
        if password != password2:
            return render(request, "registration_page.html", {"errors": ["Passwords do not match"]})

        # Create the user
        user = User.objects.create_user(userName, emailId, password)
        profile = UserProfile(user=user, full_name=fullName)
        profile.save()
        return redirect("index.html")


    return render(request, "registration_page.html")

def home(request):
    
    return render(request, "home.html")
def selection(request):
    
    return render(request, "selection.html")
def quiz(request):
    
    return render(request, "quiz.html")
def mulquiz(request):
    
    return render(request, "multipleanswer.html")
def score(request):
    
    return render(request, "score-details.html")
    
def team(request):
    
    return render(request, "team-details.html")
    


