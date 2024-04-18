from django.conf import settings
from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(
        request,
        'contact/index.html'
    )


def enviar_email(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        mensagem = request.POST.get('mensagem')

        send_mail(
            'Assunto do Email',
            f'Nome: {nome}\nEmail: {email}\nMensagem: {mensagem}',
            settings.EMAIL_HOST_USER,
            ['iwersongss@gmail.com'],  # Substitua pelo seu endereço de email
            fail_silently=False,
        )

        return HttpResponse('Email enviado com sucesso.')
    return HttpResponse('Método não permitido.')
