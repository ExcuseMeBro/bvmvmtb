# Generated by Django 5.1.5 on 2025-04-01 01:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='faq',
            name='answer_ru',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='faq',
            name='answer_uz',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='faq',
            name='question_ru',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='faq',
            name='question_uz',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
