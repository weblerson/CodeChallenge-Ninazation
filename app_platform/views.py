from django.shortcuts import render
from django.http import HttpRequest

from django.contrib.auth.decorators import login_required
from django.contrib import auth


@login_required(login_url='/auth/login')
def avaliation(request: HttpRequest):
    match request.method:
        case 'GET':
            return render(request, 'avaliacao.html')
