# Generated by Django 4.1.7 on 2023-03-18 22:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('born_at', models.DateField(null=True)),
                ('died_at', models.DateField(null=True)),
                ('contact', models.CharField(max_length=100, null=True)),
                ('bio', models.CharField(max_length=200, null=True)),
            ],
        ),
    ]
