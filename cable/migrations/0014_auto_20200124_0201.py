# Generated by Django 3.0.2 on 2020-01-24 02:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cable', '0013_auto_20200123_0140'),
    ]

    operations = [
        migrations.AlterField(
            model_name='residencdimens',
            name='corrente_nominal',
            field=models.CharField(blank=True, max_length=4, verbose_name='Corrente Nominal'),
        ),
    ]
