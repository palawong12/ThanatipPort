# Generated by Django 3.0.5 on 2020-11-10 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0020_auto_20201110_0431'),
    ]

    operations = [
        migrations.AddField(
            model_name='postimg',
            name='picture9',
            field=models.ImageField(blank=True, default='placeholder.png', null=True, upload_to='gallerys'),
        ),
    ]
