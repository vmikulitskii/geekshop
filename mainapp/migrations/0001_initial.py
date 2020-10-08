# Generated by Django 2.2.16 on 2020-10-08 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProductCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, unique=True, verbose_name='Имя')),
                ('description', models.TextField(blank=True, verbose_name='Описание')),
            ],
        ),
    ]
