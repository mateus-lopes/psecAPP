# Generated by Django 4.0 on 2021-12-09 04:26

import ckeditor.fields
import ckeditor_uploader.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Atividade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', ckeditor.fields.RichTextField()),
                ('dica', ckeditor_uploader.fields.RichTextUploadingField()),
                ('created_ata', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Dificuldade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('numero', models.DecimalField(decimal_places=0, max_digits=2)),
            ],
        ),
        migrations.CreateModel(
            name='Disciplina',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('numero', models.DecimalField(decimal_places=0, max_digits=2)),
            ],
        ),
        migrations.CreateModel(
            name='Material_Apoio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=255)),
                ('texto', ckeditor_uploader.fields.RichTextUploadingField()),
                ('created_atm', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tipo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('numero', models.DecimalField(decimal_places=0, max_digits=2)),
            ],
        ),
        migrations.CreateModel(
            name='Questao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', ckeditor.fields.RichTextField()),
                ('descricao', ckeditor.fields.RichTextField()),
                ('titulo', ckeditor_uploader.fields.RichTextUploadingField()),
                ('alt1', ckeditor_uploader.fields.RichTextUploadingField()),
                ('alt2', ckeditor_uploader.fields.RichTextUploadingField()),
                ('alt3', ckeditor_uploader.fields.RichTextUploadingField()),
                ('alt4', ckeditor_uploader.fields.RichTextUploadingField()),
                ('atividade', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='questoes', to='app_psec.atividade')),
            ],
        ),
        migrations.AddField(
            model_name='atividade',
            name='dificuldade',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app_psec.dificuldade'),
        ),
        migrations.AddField(
            model_name='atividade',
            name='disciplina',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app_psec.disciplina'),
        ),
        migrations.AddField(
            model_name='atividade',
            name='tipo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app_psec.tipo'),
        ),
    ]
