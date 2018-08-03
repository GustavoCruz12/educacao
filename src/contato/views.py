from django.urls import reverse
from django.views.generic import FormView
from django.core.mail import EmailMultiAlternatives
from django.contrib import messages

from utils.mixinscomuns import ComunsNoticiasMixin
from .forms import FormContact


class ContactView(ComunsNoticiasMixin, FormView):
    template_name = 'contato/contato.html'
    form_class = FormContact
    success_url = '/contato/'

    def get_success_url(self):
        messages.add_message(self.request, messages.SUCCESS, 'Mensagem enviada com sucesso, em breve entraremos em contato com você!')
        return reverse('contato:contato_view')

    def form_valid(self, form):

        nome = form.cleaned_data['nome']
        sobrenome = form.cleaned_data['sobrenome']
        from_email = form.cleaned_data['email']
        to_email = form.cleaned_data['secretaria']
        telefone = form.cleaned_data['telefone']
        assunto = form.cleaned_data['assunto']
        mensagem = form.cleaned_data['mensagem']

        # envio do email
        html_content = """<span style="font-size: 16px; color: #1C1C1C;">Informacao recebida de  {0} {1} </span><br /><br />
                          <span style="font-size: 16px; color: #1C1C1C;">Telefone  {2} </span><br /><br />
                          Responder a:  <span style    ="color: #6495ED; font-size: 16px"> {3} </span><br /><br />
                          <span style="color: #696969; font-size: 14px;">{4}</span>""".format(nome, sobrenome, telefone, from_email, mensagem)
        msg = EmailMultiAlternatives(assunto, html_content, 'pmsserrana@gmail.com', [to_email])
        msg.attach_alternative(html_content, 'text/html')
        msg.send()

        return super(ContactView, self).form_valid(form)














