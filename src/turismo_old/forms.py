from django import forms

from simplemathcaptcha.fields import MathCaptchaField, MathCaptchaWidget



class FormContact(forms.Form):
    nome = forms.CharField(label='Nome', max_length=80)
    email = forms.EmailField(label='email', required=True)
    telefone = forms.CharField(label='Telefone', required=False)
    assunto = forms.CharField(label='Assunto', max_length=80)
    mensagem = forms.CharField(label='Mensagem', widget=forms.Textarea())
    captcha = MathCaptchaField(widget=MathCaptchaWidget(
        question_tmpl="Quanto é: %(num1)i %(operator)s %(num2)i?",
    ))