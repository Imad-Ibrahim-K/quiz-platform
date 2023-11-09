from django.shortcuts import render

# Create your views here.
def signin(request):


    return render(request, "index.html")


def signup(request):

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
    


