from django.shortcuts import render
from app_psec.models import Questao, Material_Apoio, Tipo, Atividade, Dificuldade, Disciplina
# Create your views here.

def home(request):
    diciplinas = Disciplina.objects.all()
    atividades = Atividade.objects.all()
    return render(request, 'home.html', {'atividades': atividades, 'diciplinas': diciplinas})

def contato(request):
    return render(request, 'contato.html')

def atividade(request, atividade_id):
    diciplinas = Disciplina.objects.all()
    atividade = Atividade.objects.get(pk=atividade_id)
    return render(request, 'atividade.html', {'atividade': atividade, 'diciplinas': diciplinas})

def material(request, material_id):
    diciplinas = Disciplina.objects.all()
    material = Material_Apoio.objects.get(pk=material_id)
    return render(request, 'material.html', {'material': material, 'diciplinas': diciplinas})

def todas_atividades(request):
    diciplinas = Disciplina.objects.all()
    atividades = Atividade.objects.all()
    return render(request, 'todas_atividades.html', {'atividades': atividades, 'diciplinas': diciplinas})

def todos_materiais(request):
    diciplinas = Disciplina.objects.all()
    materiais = Material_Apoio.objects.all()
    return render(request, 'todos_materiais.html', {'materiais': materiais, 'diciplinas': diciplinas})
