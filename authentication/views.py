from django.shortcuts import render, redirect
from django.http import HttpRequest

from django.contrib.auth.models import User
from .forms import RegisterForm


def register(request: HttpRequest):
    match request.method:
        case 'GET':
            if request.user.is_authenticated:
                # Redirecionar pra página principal
                
                ...

            return render(request, 'cadastro.html')

        case 'POST':
            form: RegisterForm = RegisterForm(request.POST)
            if not form.is_valid():
                return redirect('/auth/register')

            try:
                _username, _email = User.objects.filter(username=form.data.get('username')), User.objects.filter(email=form.data.get('email'))

                if _username or _email:
                    # Levantar erro sobre usuário existente

                    ...

                user: User = User.objects.create_user(
                    username=form.data.get('username'),
                    email=form.data.get('email'),
                    password=form.data.get('password')
                )

                # Mostrar mensagem de sucesso

                return redirect('/auth/login')

            except:
                # Mostrar mensagem de erro no sistema

                return redirect('/auth/register')


def login(request: HttpRequest):
    ...
