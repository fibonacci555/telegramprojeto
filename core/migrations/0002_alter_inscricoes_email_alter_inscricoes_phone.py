# Generated by Django 4.1.3 on 2023-06-30 02:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inscricoes',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name='inscricoes',
            name='phone',
            field=models.CharField(max_length=20, unique=True),
        ),
    ]
