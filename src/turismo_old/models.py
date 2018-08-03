from django.db import models


class CategoriaAtracao(models.Model):
    tag = models.CharField('tag', max_length=80)
    descricao = models.CharField('descrição', max_length=80)

    def __str__(self):
        return self.tag

    class Meta:
        db_table = 'tb_turismo_categoria'
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'


class Atracao(models.Model):
    tag = models.ForeignKey(CategoriaAtracao,
                            on_delete=models.CASCADE,
                            related_name='atracoes')

    atracao = models.CharField('atração', max_length=180)
    descricao = models.TextField('descricao', max_length=4000)
    imagem = models.ImageField('imagem', upload_to='uploads/turismo')

    def __str__(self):
        return self.atracao

    class Meta:
        db_table = 'tb_turismo_atracao'
        verbose_name = 'Atração'
        verbose_name_plural = 'Atrações'


class PontoTuristico(models.Model):
    nome = models.CharField('nome', max_length=180)
    descricao = models.TextField('descrição', max_length=4000)
    imagem = models.ImageField('imagem', upload_to='uploads/turismo/pontos')

    def __str__(self):
        return self.nome

    class Meta:
        db_table = 'tb_turismo_ponto_turistico'
        verbose_name = 'Ponto Turistico'
        verbose_name_plural = 'Pontos Turisticos'
