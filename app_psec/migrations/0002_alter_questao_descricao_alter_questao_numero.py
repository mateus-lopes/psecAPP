# Generated by Django 4.0 on 2021-12-09 04:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_psec', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questao',
            name='descricao',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='questao',
            name='numero',
            field=models.CharField(max_length=100),
        ),
    ]
