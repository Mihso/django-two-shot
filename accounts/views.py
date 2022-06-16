from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth import login
from receipts.models import Receipt
# Create your views here.
def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = User.objects.create_user(username = request.POST.get("username"), password = request.POST.get("password"),)
            new_user.save()
            login(request, new_user)
            return redirect("home")
    else:
        form = UserCreationForm()
    context = {"form" : form,}
    return render(request, "registration/signup.html", context)

def practice(request):
    list = Receipt.objects.all()
    dabadoo = []
    for l in range(0, 10):
        dabadoo.append("horse")
    print("fish")
    context = {
        "practices_list": list,
        "numby" : dabadoo,
    }

    response = render(request, "accounts/list.html", context)

    return response
            
