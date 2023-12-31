# Generated by Django 4.2.2 on 2023-07-15 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Entradas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulos', models.CharField(default='DEFAULT VALUE', max_length=100)),
                ('contenido', models.TextField(default='DEFAULT VALUE')),
                ('img', models.FileField(upload_to='')),
                ('slug', models.CharField(default='DEFAULT VALUE', max_length=5000)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'entradas',
            },
        ),
    ]
