# Generated by Django 3.1.7 on 2021-03-26 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='upload',
            field=models.ImageField(upload_to=''),
        ),
    ]
