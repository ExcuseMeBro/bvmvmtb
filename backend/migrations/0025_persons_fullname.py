# Generated by Django 5.2 on 2025-04-06 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0024_persons_avatar'),
    ]

    operations = [
        migrations.AddField(
            model_name='persons',
            name='fullname',
            field=models.CharField(default='', max_length=100, verbose_name="To'liq ism"),
        ),
    ]
