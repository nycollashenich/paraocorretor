# Generated by Django 5.0.6 on 2024-07-03 21:54

import core.models
import stdimage.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Corretor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criado', models.DateField(auto_now_add=True, verbose_name='Criado em')),
                ('modificado', models.DateField(auto_now=True, verbose_name='Modificado em')),
                ('ativo', models.BooleanField(default=True, verbose_name='Ativo?')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome')),
                ('idade', models.DecimalField(decimal_places=0, max_digits=100, verbose_name='Idade')),
                ('profissao', models.CharField(max_length=100, verbose_name='Profissão')),
                ('biografia', models.TextField(verbose_name='Biografia')),
                ('personalidade', models.TextField(verbose_name='Personalidade')),
                ('interesse', models.CharField(max_length=100, verbose_name='Interesse')),
                ('missao', models.CharField(max_length=100, verbose_name='Missão')),
                ('visao', models.CharField(max_length=100, verbose_name='Visão')),
                ('valores', models.CharField(max_length=100, verbose_name='Valores')),
                ('imagem', stdimage.models.StdImageField(force_min_size=False, upload_to=core.models.get_file_path, variations={'thumb': {'crop': True, 'height': 480, 'width': 480}}, verbose_name='Imagem')),
            ],
            options={
                'verbose_name': 'Corretor',
            },
        ),
    ]
