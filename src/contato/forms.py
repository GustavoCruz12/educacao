from django import forms

from simplemathcaptcha.fields import MathCaptchaField, MathCaptchaWidget

SECRETARIA_CHOICES = (
        ('gabinete@serrana.sp.gov.br', 'Gabinete'),
        ('nucleoexecutivo@serrana.sp.gov.br', 'Administração e Finanças'),
        ('educacao@serrana.sp.gov.br', 'Educação'),
        ('infraestrutura@serrana.sp.gov.br', 'Infraestrutura'),
        ('social@serrana.sp.gov.br', 'Assistência Social'),
        ('dpsaude@serrana.sp.gov.br', 'Saúde'),
        ('esportes@serrana.sp.gov.br', 'Esportes, Cultura e Turismo'),
)


class FormContact(forms.Form):
    nome = forms.CharField(label='Nome', max_length=80)
    sobrenome = forms.CharField(label='Sobrenome', max_length=80)
    email = forms.EmailField(label='email', required=True)
    telefone = forms.EmailField(label='Telefone', required=False)
    secretaria = forms.ChoiceField(label='Secretaria', widget=forms.Select, choices=SECRETARIA_CHOICES)
    assunto = forms.CharField(label='Assunto', max_length=80)
    mensagem = forms.CharField(label='Mensagem', widget=forms.Textarea())
    captcha = MathCaptchaField(widget=MathCaptchaWidget(
        question_tmpl="Quanto é: %(num1)i %(operator)s %(num2)i?",
    ))