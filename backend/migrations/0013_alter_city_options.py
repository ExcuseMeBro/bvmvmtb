# Generated by Django 5.2 on 2025-04-04 21:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0012_city'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='city',
            options={'ordering': ['name'], 'verbose_name': 'Tuman', 'verbose_name_plural': 'Tumanlar'},
        ),
    ]
