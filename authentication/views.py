from django.shortcuts import render, redirect
from django.http import HttpRequest

from django.contrib.auth.models import User

from django.contrib import messages, auth
from django.contrib.messages import constants

from utils import Utils


def register(request: HttpRequest):
    match request.method:
        case 'GET':
            if request.user.is_authenticated:
                # Redirecionar pra página principal
                
                return redirect('/avaliation')

            return render(request, 'cadastro.html')

        case 'POST':
            username = request.POST.get('username')
            email = request.POST.get('email')
            password = request.POST.get('password')
            confirm_password = request.POST.get('confirm_password')

            if not Utils.validate_email(email):
                messages.add_message(
                    request,
                    constants.WARNING,
                    'Digite um e-mail válido!'
                )

            if not any([Utils.validate_password(password), Utils.validate_password(confirm_password)]):
                messages.add_message(
                    request, 
                    constants.WARNING, 
                    'É preciso que sua senha tenha no mínimo uma letra maiúscula, um número e um caractere especial.'
                )

                return redirect('/auth/register')

            if not password == confirm_password:
                messages.add_message(
                    request, 
                    constants.WARNING, 
                    'As senhas não coincidem.'
                )

                return redirect('/auth/register')

            try:
                _username, _email = User.objects.filter(username=username), User.objects.filter(email=email)

                if _username or _email:
                    # Levantar erro sobre usuário existente
                    messages.add_message(request, constants.WARNING, 'Já existe um usuário com esse email ou nome de usuário cadastrado. Use outro!')

                    return redirect('/auth/register')

                User.objects.create_user(
                    username=username,
                    email=email,
                    password=password
                )

                # Mostrar mensagem de sucesso
                messages.add_message(request, constants.SUCCESS, 'Usuário cadastrado com sucesso!')

                return redirect('/auth/login')

            except:
                # Mostrar mensagem de erro no sistema
                messages.add_message(request, constants.ERROR, 'Erro interno do sistema')

                return redirect('/auth/register')


def login(request: HttpRequest):
    match request.method:
        case 'GET':
            if request.user.is_authenticated:
                # Redirecionar pra página principal
                
                return redirect('/avaliation')

            return render(request, 'login.html')

        case 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            if not Utils.validate_password(password):
                messages.add_message(
                    request, 
                    constants.WARNING, 
                    'É preciso que sua senha tenha no mínimo uma letra maiúscula, um número e um caractere especial.'
                )

                return redirect('/auth/login')

            user = auth.authenticate(username=username, password=password)
            if not user:
                messages.add_message(request, constants.WARNING, "Usuário passado não existe! Verifique seu usuário ou senha.")
                return redirect('/auth/login')

            auth.login(request, user)

            return redirect('/avaliation')
