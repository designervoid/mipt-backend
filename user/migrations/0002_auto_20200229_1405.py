# Generated by Django 3.0.3 on 2020-02-29 14:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='pub_date',
        ),
        migrations.AlterField(
            model_name='user',
            name='room',
            field=models.FloatField(),
        ),
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField()),
                ('theme', models.CharField(max_length=40)),
                ('tags', models.CharField(max_length=20)),
                ('created_data', models.DateTimeField(auto_now=True)),
                ('id_order', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='user.User')),
            ],
        ),
    ]