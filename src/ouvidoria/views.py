from django.urls import reverse
from django.views.generic import FormView, TemplateView
from django.core.mail import EmailMultiAlternatives
from django.contrib import messages

from utils.mixinscomuns import ComunsNoticiasMixin

from .forms import OuvidoriaForm


class OuvidoriaHome(ComunsNoticiasMixin, TemplateView):
    template_name = 'ouvidoria/home.html'


class OuvidoriaView(ComunsNoticiasMixin, FormView):
    template_name = 'ouvidoria/formulario.html'
    form_class = OuvidoriaForm
    success_url = '/ouvidoria/home/'

    def get_success_url(self):
        messages.add_message(self.request, messages.SUCCESS, 'Mensagem enviada com sucesso, em breve entraremos em contato com você!')
        return reverse('ouvidoria:home')

    def form_valid(self, form):

        nome = form.cleaned_data['nome']
        sobrenome = form.cleaned_data['sobrenome']
        from_email = form.cleaned_data['email']
        secretaria = form.cleaned_data['secretaria']
        telefone = form.cleaned_data['telefone']
        assunto = form.cleaned_data['assunto']
        mensagem = form.cleaned_data['mensagem']

        # envio do email
        html_content = """<span style="font-size: 16px; color: #1C1C1C;"><b>Manifestação enviada por:</b> {0} {1} </span><br /><br />
                          <span style="font-size: 16px; color: #1C1C1C;"><b>Telefone:</b> {2} </span><br /><br />
                          <span style="font-size: 16px; color: #1C1C1C;"><b>email:</b> {3} </span><br /><br />
                          <span style="font-size: 16px; color: #1C1C1C;"><b>Órgão para o qual a manifestação foi enviada:</b> <i>{4}</i> </span><br /><br />
                          <span style="font-size: 16px; color: #1C1C1C;"><b>Conteúdo da manifestação:</b><br /><hr> {5}</span>""".format(nome, sobrenome, telefone,
                                                                                              from_email, secretaria, mensagem)
        msg = EmailMultiAlternatives(assunto, html_content, 'pmsserrana@gmail.com', ['ouvidoria@serrana.sp.gov.br', ])
        msg.attach_alternative(html_content, 'text/html')
        msg.send()

        return super(OuvidoriaView, self).form_valid(form)

