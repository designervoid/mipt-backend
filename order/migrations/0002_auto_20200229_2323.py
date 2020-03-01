# Generated by Django 3.0.3 on 2020-02-29 23:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='claim',
            name='answer',
            field=models.CharField(default=1, max_length=40),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='claim',
            name='progress',
            field=models.CharField(choices=[('cd', 'considuration'), ('pf', 'performed'), ('rj', 'rejected'), ('rd', 'ready')], default=1, max_length=2),
            preserve_default=False,
        ),
    ]