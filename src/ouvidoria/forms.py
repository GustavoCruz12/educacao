from django import forms
from simplemathcaptcha.fields import MathCaptchaField, MathCaptchaWidget


MANIFESTACOES_CHOICES = (
    ('reclamacao', 'Reclamação'),
    ('solicitacao', 'Solicitação'),
    ('denuncia', 'Denúncia'),
    ('elogio', 'Elogio'),
    ('sugestao', 'Sugestão'),
)

SECRETARIA_CHOICES = (
        ('Gabinete do Prefeito', 'Gabinete do Prefeito'),
        ('Secretaria de Administração e Finanças', 'Secretaria de Administração e Finanças'),
        ('Secretaria de Educação', 'Secretaria de Educação'),
        ('Secretaria de Infraestrutura', 'Secretaria de Infraestrutura'),
        ('Secretaria de Assistência Social', 'Secretaria de Assistência Social'),
        ('Secretaria de Saúde', 'Secretaria de Saúde'),
        ('Secretaria de Esportes, Cultura e Turismo', 'Secretaria de Esportes, Cultura e Turismo'),
)


class OuvidoriaForm(forms.Form):
    nome = forms.CharField(label='*Nome', max_length=80)
    sobrenome = forms.CharField(label='*Sobrenome', max_length=80)
    email = forms.EmailField(label='email', required=False, max_length=80)
    telefone = forms.CharField(label='*Telefone para contato', max_length=11)
    secretaria = forms.ChoiceField(label='*Órgão para o qual você quer enviar sua manifestação', widget=forms.Select, choices=SECRETARIA_CHOICES)
    assunto = forms.ChoiceField(label='*Sobre qual assunto você quer falar ', widget=forms.Select, choices=MANIFESTACOES_CHOICES)
    mensagem = forms.CharField(label='*Descreva abaixo o conteúdo de sua manifestação.', widget=forms.Textarea())
    captcha = MathCaptchaField(widget=MathCaptchaWidget(
           question_tmpl="*Quanto é: %(num1)i %(operator)s %(num2)i?",
    ))
