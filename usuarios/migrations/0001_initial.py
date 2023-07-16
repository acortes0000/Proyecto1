# Generated by Django 4.2.2 on 2023-07-15 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuarios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(default='DEFAULT VALUE', max_length=100)),
                ('img', models.FileField(upload_to='')),
                ('mail', models.CharField(default='DEFAULT VALUE', max_length=50)),
                ('descripcion', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'usuarios',
            },
        ),
    ]
