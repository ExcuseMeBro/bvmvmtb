# Generated by Django 5.2 on 2025-04-06 03:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0022_alter_vote_options_districtleader_leader'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='districtleader',
            options={'ordering': ['fullname'], 'verbose_name': 'District Leader', 'verbose_name_plural': 'Tuman mudirlari'},
        ),
        migrations.AddField(
            model_name='districtleader',
            name='address',
            field=models.TextField(blank=True, null=True, verbose_name='Manzil'),
        ),
    ]
