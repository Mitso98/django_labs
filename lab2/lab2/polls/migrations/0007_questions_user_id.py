# Generated by Django 4.1.7 on 2023-03-25 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0006_remove_questions_vote'),
    ]

    operations = [
        migrations.AddField(
            model_name='questions',
            name='user_id',
            field=models.IntegerField(default=0),
        ),
    ]
