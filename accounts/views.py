from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm


def home(request):
    return render(request, "home.html")


def register(request):
    form = RegisterForm()

    if request.method == "POST":
        form = RegisterForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, "Registration Successful! Please Login.")
            return redirect("login")
        else:
            messages.error(request, "Registration Failed! Please check the details.")

    return render(request, "register.html", {"form": form})


def user_login(request):
    if request.method == "POST":
        emp_id = request.POST.get("emp_id")
        password = request.POST.get("password")

        user = authenticate(request, username=emp_id, password=password)

        if user is not None:
            login(request, user)
            return redirect("dashboard")
        else:
            messages.error(request, "Invalid Employee ID or Password!")

    return render(request, "login.html")


def user_logout(request):
    logout(request)
    return redirect("home")


@login_required
def dashboard(request):
    if request.user.role == "admin":
        return redirect("admin_dashboard")
    else:
        return redirect("consultant_dashboard")