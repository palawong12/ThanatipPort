# Generated by Django 3.1.1 on 2020-10-13 01:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_auto_20201013_0823'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='Thumnail',
            field=models.ImageField(blank=True, default='/images/placeholder.png', null=True, upload_to='images'),
        ),
    ]
