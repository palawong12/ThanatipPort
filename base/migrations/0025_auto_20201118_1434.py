# Generated by Django 3.0.5 on 2020-11-18 07:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0024_imgcomment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imgcomment',
            name='post',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='base.PostImg'),
        ),
    ]