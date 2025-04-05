from django.db import migrations, models

class Migration(migrations.Migration):
    dependencies = [
        ('backend', '0019_remove_news_category_delete_newscategory'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('option', models.CharField(choices=[('excellent', "Zo'r"), ('good', 'Yaxshi'), ('satisfactory', 'Qoniqarli'), ('unsatisfactory', 'Qoniqarsiz')], max_length=20)),
                ('count', models.IntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['-count'],
                'verbose_name': 'Ovoz',
                'verbose_name_plural': 'Ovozlar',
            },
        ),
    ]