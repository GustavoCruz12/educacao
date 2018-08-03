from django.views.generic import TemplateView
from django.core.mail import EmailMultiAlternatives
from django.shortcuts import render

from .forms import FormContact


def contato(request):
    if request.method == 'POST':
        form = FormContact(request.POST)
        if form.is_valid():
            nome = form.cleaned_data['nome']
            from_email = form.cleaned_data['email']
            to_email = form.cleaned_data['secretaria']
            assunto = form.cleaned_data['assunto']
            mensagem = form.cleaned_data['mensagem']

            # envio do email
            html_content = '<span style="font-size: 16px; color: #1C1C1C;">Informacao recebida de  {0} </span><br /><br />Responder a:  <span style    ="color: #6495ED; font-size: 16px"> {1} </span><br /><br /><span style="color: #696969; font-size: 14px;">{2}</span>'.format(nome, from_email, mensagem)
            msg = EmailMultiAlternatives(assunto, html_content, 'faleconosco@serrana.sp.gov.br', to_email)
            msg.attach_alternative(html_content, 'text/html')
            msg.send()
    else:
        form = FormContact()

    return render(request,
                  'contato/contato.html',
                  {'form':form})








