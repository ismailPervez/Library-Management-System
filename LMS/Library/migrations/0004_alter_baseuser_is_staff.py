# Generated by Django 4.0.2 on 2022-02-22 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Library', '0003_alter_takenbook_date_returned'),
    ]

    operations = [
        migrations.AlterField(
            model_name='baseuser',
            name='is_staff',
            field=models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status'),
        ),
    ]
