from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models


# Create your models here.

from django.db import models
from django.urls import reverse

class Disciplina(models.Model):
    nome = models.CharField(max_length=100)
    numero = models.DecimalField(max_digits=2, decimal_places=0)

    def __str__(self):
        return self.nome

class Dificuldade(models.Model):
    nome = models.CharField(max_length=100)
    numero = models.DecimalField(max_digits=2, decimal_places=0)

    def __str__(self):
        return self.nome

class Tipo(models.Model):
    nome = models.CharField(max_length=100)
    numero = models.DecimalField(max_digits=2, decimal_places=0)

    def __str__(self):
        return self.nome

class Atividade(models.Model):
    titulo = RichTextField()
    descricao_seo = models.CharField(max_length=100)
    # autor = models.ForeignKey(
    #     'auth.User',
    #     on_delete=models.PROTECT,
    # )
    tipo = models.ForeignKey(Tipo, on_delete=models.PROTECT)
    disciplina = models.ForeignKey(Disciplina, on_delete=models.PROTECT)
    dificuldade = models.ForeignKey(Dificuldade, on_delete=models.PROTECT)
    dica = RichTextUploadingField()
    created_ata = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.descricao_seo

    def get_absolute_url(self):
        return reverse('atividades', args=[str(self.id)])

class Questao(models.Model):
    numero = models.CharField(max_length=100)
    descricao_seo = models.CharField(max_length=100)
    titulo = RichTextUploadingField()
    alt1 = RichTextUploadingField()
    alt2 = RichTextUploadingField()
    alt3 = RichTextUploadingField()
    alt4 = RichTextUploadingField()
    show = models.CharField(max_length=100)
    atividade = models.ForeignKey(Atividade, on_delete=models.PROTECT, related_name="questoes")
    def __str__(self):
        return self.descricao_seo

class Material_Apoio(models.Model):
    titulo = RichTextUploadingField()
    descricao_seo = models.CharField(max_length=100)
    disciplina = models.ForeignKey(Disciplina, on_delete=models.PROTECT)
    resumo = RichTextField()
    texto = RichTextUploadingField()
    created_atm = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.descricao_seo
    

    
    