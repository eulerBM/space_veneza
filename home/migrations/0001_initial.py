# Generated by Django 4.2.5 on 2023-09-25 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='noticia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=350)),
                ('corpo', models.TextField(max_length=10000)),
                ('image', models.ImageField(upload_to='static/img/')),
                ('date', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
