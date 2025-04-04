from django.db import migrations, models
from django.utils.translation import gettext_lazy as _

class Migration(migrations.Migration):
    dependencies = [
        ('backend', '0011_usefullink'),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(_('Name'), max_length=100)),
                ('is_active', models.BooleanField(_('Active'), default=True)),
                ('created_at', models.DateTimeField(_('Created At'), auto_now_add=True)),
                ('updated_at', models.DateTimeField(_('Updated At'), auto_now=True)),
                ('region', models.ForeignKey('backend.Region', on_delete=models.CASCADE, related_name='cities', verbose_name=_('Region'))),
            ],
            options={
                'verbose_name': _('City'),
                'verbose_name_plural': _('Cities'),
                'ordering': ['name'],
            },
        ),
    ]