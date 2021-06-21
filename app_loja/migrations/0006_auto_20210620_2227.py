# Generated by Django 3.2.4 on 2021-06-20 22:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_loja', '0005_alter_tranzacao_valor'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tranzacao',
            name='tipo',
        ),
        migrations.AddField(
            model_name='tranzacao',
            name='descricao',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='tranzacao',
            name='natureza',
            field=models.TextField(blank=True),
        ),
    ]