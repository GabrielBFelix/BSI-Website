# Generated by Django 2.2.7 on 2019-12-05 17:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bsi', '0004_aluno_vagaestagio'),
    ]

    operations = [
        migrations.RenameField(
            model_name='estagio',
            old_name='tipo',
            new_name='nome',
        ),
    ]
