from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .forms import NewUserForm
from .models import Profile


def register(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            profile_obj = Profile(user=user)
            profile_obj.save()
            return redirect('/')
    form = NewUserForm()
    context = {
        "form": form
    }
    return render(request, "users/register.html", context=context)


@login_required
def profile(request):
    return render(request, "users/profile.html")