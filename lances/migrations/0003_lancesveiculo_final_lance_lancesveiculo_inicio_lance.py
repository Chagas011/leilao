# Generated by Django 4.1 on 2022-08-21 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lances', '0002_alter_lancesveiculo_seu_lance'),
    ]

    operations = [
        migrations.AddField(
            model_name='lancesveiculo',
            name='final_lance',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='lancesveiculo',
            name='inicio_lance',
            field=models.DateField(blank=True, null=True),
        ),
    ]
