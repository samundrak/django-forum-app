from django.shortcuts import render, redirect

from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterForm


# Create your views here.
def register_view(request):
    if request.user.is_authenticated:
        return redirect('/')
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {
        "form": form
    })
