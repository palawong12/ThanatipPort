# Generated by Django 3.1.1 on 2020-10-13 01:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_auto_20201013_0830'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='Thumnail',
            field=models.ImageField(blank=True, default='placeholder.png', null=True, upload_to='images'),
        ),
    ]
