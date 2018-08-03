from django import forms
from simplemathcaptcha.fields import MathCaptchaField

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
    nome = forms.CharField(label='nome', max_length=80)
    email = forms.EmailField(label='email', required=True, max_length=80)
    secretaria = forms.ChoiceField(label='secretaria', widget=forms.Select, choices=SECRETARIA_CHOICES )
    assunto = forms.ChoiceField(label='assunto', widget=forms.Select, choices=MANIFESTACOES_CHOICES)
    mensagem = forms.CharField(label='mensagem', widget=forms.Textarea())
    captcha = MathCaptchaField()
