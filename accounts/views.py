from django.contrib import messages
from django.contrib.auth import authenticate, get_user_model, login, logout
from django.shortcuts import redirect, render

from .forms import RegisterCustomerForm

User = get_user_model()


def register_customer(request):
    if request.method == "POST":
        form = RegisterCustomerForm(request.POST)
        if form.is_valid():
            var = form.save(commit=False)
            var.is_customer = True
            var.username = var.email
            var.save()
            messages.success(request, "Conta criada com sucesso!")
            return redirect("login")
        else:
            messages.error(request, "Erro ao criar conta!")
            return redirect("register-customer")
    else:
        form = RegisterCustomerForm()
        return render(request, "accounts/register_customer.html", {"form": form})


def login_user(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None and user.is_active:
            login(request, user)
            return redirect("dashboard")
        else:
            messages.error(request, "Usuário ou senha inválidos!")
            return redirect("login")
    else:
        return render(request, "accounts/login.html")


def logout_user(request):
    logout(request)
    messages.success(request, "Deslogado com sucesso!")
    return redirect("login")
