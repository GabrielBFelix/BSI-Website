# Generated by Django 2.2.7 on 2019-12-05 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bsi', '0005_auto_20191205_1419'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aluno',
            name='vagaEstagio',
            field=models.ForeignKey(null=True, on_delete=models.SET('0'), to='bsi.Estagio'),
        ),
    ]