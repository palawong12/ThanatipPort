# Generated by Django 3.1.1 on 2020-10-13 01:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0007_auto_20201013_0853'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='thumbnail',
            field=models.ImageField(blank=True, default='/static/images/placeholder.png', null=True, upload_to='images/'),
        ),
    ]
