# Generated by Django 2.2.7 on 2019-11-27 00:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aluno',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('username', models.CharField(max_length=100)),
                ('senha', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('username', models.CharField(max_length=100)),
                ('senha', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Projeto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('numVagas', models.IntegerField(default=0)),
                ('descricao', models.CharField(max_length=300)),
                ('coordenador', models.ForeignKey(on_delete=models.SET('0'), to='bsi.Professor')),
            ],
        ),
        migrations.CreateModel(
            name='Noticia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('descricao', models.CharField(max_length=300)),
                ('autor', models.ForeignKey(on_delete=models.SET('0'), to='bsi.Professor')),
            ],
        ),
        migrations.CreateModel(
            name='Laboratorio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('descricao', models.CharField(max_length=300)),
                ('coordenador', models.ForeignKey(on_delete=models.SET('0'), to='bsi.Professor')),
            ],
        ),
    ]
