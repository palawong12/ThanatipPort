# Generated by Django 3.0.8 on 2020-10-13 03:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0009_auto_20201013_0955'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='thumbnail',
            field=models.ImageField(blank=True, default='/images/placeholder.png', null=True, upload_to='images'),
        ),
    ]
