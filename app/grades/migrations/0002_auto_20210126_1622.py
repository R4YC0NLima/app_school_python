# Generated by Django 2.2.13 on 2021-01-26 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grades', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aluno',
            name='status',
            field=models.CharField(max_length=30),
        ),
    ]
