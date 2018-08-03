from django.shortcuts import render
from django.core.mail import EmailMultiAlternatives
from django.contrib import messages

from django.shortcuts import redirect

from .models import CategoriaAtracao, Atracao, PontoTuristico
from .forms import FormContact


def turismo(request):

    if request.method == 'GET':
        form = FormContact()
    else:
        form = FormContact(request.POST)
        if form.is_valid():
            nome = form.cleaned_data['nome']
            email = form.cleaned_data['email']
            telefone = form.cleaned_data['telefone']
            assunto = form.cleaned_data['assunto']
            mensagem = form.cleaned_data['mensagem']

            # envio do email
            html_content = """<span style="font-size: 16px; color: #1C1C1C;"><b>Mensagem enviada por:</b> {0} </span><br /><br />
                          <span style="font-size: 16px; color: #1C1C1C;"><b>email:</b> {1} </span><br /><br />
                          <span style="font-size: 16px; color: #1C1C1C;"><b>Telefone: </b> <i>{2}</i> </span><br /><br />
                          <span style="font-size: 16px; color: #1C1C1C;"><b>Conteúdo da Mensagem:</b><br /><hr> {3}</span>""".format(nome, email, telefone, mensagem)
            msg = EmailMultiAlternatives(assunto, html_content, 'pmsserrana@gmail.com', ['willian.firmino@serrana.sp.gov.br', ])
            msg.attach_alternative(html_content, 'text/html')
            msg.send()
            messages.add_message(request,
                                 messages.SUCCESS,
                                 'Mensagem enviada com sucesso, em breve entraremos em contato com você!')

            return redirect('turismo:turismo')

    categorias = CategoriaAtracao.objects.all().distinct().order_by('tag')
    atracoes = Atracao.objects.all()

    return render(request, 'turismo/turismo.html',
                  {'atracoes': atracoes,
                   'categorias': categorias,
                   'form': form,
                   })


def pontos_turisticos(request):
    pontos_turisticos = PontoTuristico.objects.all()
    return render(request, 'turismo/pontos.html',
                  {'pontos_turisticos': pontos_turisticos})
