from django.contrib import admin
from app_psec.models import Questao, Material_Apoio, Tipo, Atividade, Dificuldade, Disciplina

# Register your models here.

admin.site.register(Questao)
admin.site.register(Material_Apoio)
admin.site.register(Atividade)
admin.site.register(Tipo)
admin.site.register(Dificuldade)
admin.site.register(Disciplina)


