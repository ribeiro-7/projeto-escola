# Generated by Django 5.1.7 on 2025-03-30 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cursos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Aluno',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=30)),
                ('rg', models.CharField(max_length=9)),
                ('cpf', models.CharField(max_length=11)),
                ('data_nascimento', models.DateField()),
            ],
        ),
        migrations.AlterModelOptions(
            name='curso',
            options={},
        ),
        migrations.RemoveField(
            model_name='curso',
            name='ativo',
        ),
        migrations.RemoveField(
            model_name='curso',
            name='atualizacao',
        ),
        migrations.RemoveField(
            model_name='curso',
            name='criacao',
        ),
        migrations.RemoveField(
            model_name='curso',
            name='titulo',
        ),
        migrations.RemoveField(
            model_name='curso',
            name='url',
        ),
        migrations.AddField(
            model_name='curso',
            name='codigo_curso',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AddField(
            model_name='curso',
            name='descricao',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='curso',
            name='nivel',
            field=models.CharField(choices=[('B', 'Básico'), ('I', 'Intermediário'), ('A', 'Avançado')], default='B', max_length=1),
        ),
        migrations.DeleteModel(
            name='Avaliacao',
        ),
    ]
