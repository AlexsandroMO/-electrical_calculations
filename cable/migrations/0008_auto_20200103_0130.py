# Generated by Django 3.0.1 on 2020-01-03 01:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cable', '0007_auto_20200103_0122'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tensao',
            name='volts',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
