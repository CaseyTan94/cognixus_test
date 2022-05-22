# Generated by Django 3.2.13 on 2022-05-22 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateField(auto_created=True)),
                ('title', models.CharField(max_length=100)),
                ('body', models.CharField(max_length=100)),
                ('is_completed', models.BooleanField(default=False)),
                ('last_modified', models.DateField(auto_now=True)),
            ],
        ),
    ]
