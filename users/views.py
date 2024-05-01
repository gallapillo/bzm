from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import NewUserForm


def register(request):
    print(f"1 {request.method}")
    if request.method == "POST":
        form = NewUserForm(request.POST)
        print(f"2 {form.is_valid()} - {form.errors}")
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')
    form = NewUserForm()
    context = {
        "form": form
    }
    return render(request, "users/register.html", context=context)


@login_required
def profile(request):
    context = {

    }
    return render(request, "users/profile.html", context=context)