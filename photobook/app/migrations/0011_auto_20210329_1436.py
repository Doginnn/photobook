# Generated by Django 3.1.7 on 2021-03-29 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_auto_20210329_0947'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='upload',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='Foto'),
        ),
    ]