from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm 
# Create your views here.
def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = User.objects.create_user(username = request.POST.get("username"), password = request.POST.get("password"))
            new_user.save()
            return redirect("home")
    else:
        form = UserCreationForm()
    context = {"form" : form,}
    return render(request, "registration/signup.html", context)
            
