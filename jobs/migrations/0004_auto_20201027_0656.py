# Generated by Django 2.2.16 on 2020-10-27 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0003_auto_20201016_1056'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='vacancy',
            field=models.CharField(choices=[('part-time', 'part-time'), ('full-time', 'full-time')], max_length=200),
        ),
    ]
