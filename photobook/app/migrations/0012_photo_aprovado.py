# Generated by Django 3.1.7 on 2021-03-31 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_auto_20210329_1436'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='aprovado',
            field=models.BooleanField(blank=True, default=False, null=True, verbose_name='Aprovado'),
        ),
    ]
