# Generated by Django 4.0.2 on 2022-02-21 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Student', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='password',
            field=models.CharField(max_length=60, null=True),
        ),
    ]
