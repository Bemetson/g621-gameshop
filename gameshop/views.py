from django.http import HttpResponse, Http404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.template import loader, Context
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

from gameshop.models import Game

def about(request):
    return HttpResponse("about page")

def home(request):
    #return render(request, "gameshop/home.html", {}, content_type = 'text/html')
    if request.user != None:
        print(request.user.username + " is logged in")
    return render(request, "gameshop/home.html", {"user": request.user.username})

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/')
    else:
        form = UserCreationForm()
    return render(request, "gameshop/register.html", {"form": form})
# Create your views here.

def gamescreen(request):
    return render(request, "gameshop/game.html", {})

def inventory(request):
    gamelist = Game.objects.all()
    template = loader.get_template("gameshop/inventory.html")
    context = {"gamelist": gamelist}
    return HttpResponse(template.render(context))
    
#@login_required(login_url='/login/')
def logout_page(request):
    print("Attempt to logout")
    logout(request)
    return render(request, "gameshop/authentication/logout_page.html")
