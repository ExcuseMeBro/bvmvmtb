from django.db import migrations, models
from django.utils.translation import gettext_lazy as _

class Migration(migrations.Migration):
    dependencies = [
        ('backend', '0008_remove_region_name_ru_remove_region_name_uz'),
    ]

    operations = [
        migrations.CreateModel(
            name='Statistics',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(_('Name'), max_length=100)),
                ('quantity', models.IntegerField(_('Quantity'), default=0)),
                ('created_at', models.DateTimeField(_('Created At'), auto_now_add=True)),
                ('updated_at', models.DateTimeField(_('Updated At'), auto_now=True)),
            ],
            options={
                'verbose_name': _('Statistics'),
                'verbose_name_plural': _('Statistics'),
                'ordering': ['name'],
            },
        ),
    ]