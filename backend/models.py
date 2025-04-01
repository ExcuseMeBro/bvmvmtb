from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator, FileExtensionValidator
from django.utils.translation import gettext as _

class Region(models.Model):
    name = models.CharField(_('Name'), max_length=100)
    name_uz = models.CharField(_('Name (Uzbek)'), max_length=100)
    name_ru = models.CharField(_('Name (Russian)'), max_length=100)
    code = models.CharField(_('Region Code'), max_length=10, unique=True, help_text=_('Unique identifier for the region'))
    is_active = models.BooleanField(_('Active'), default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['name']
        verbose_name = _('Region')
        verbose_name_plural = _('Regions')
    
    def __str__(self):
        return self.name

class FAQ(models.Model):
    question = models.CharField(max_length=200)
    answer = models.TextField()
    order = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['order', '-created_at']
        verbose_name = 'FAQ'
        verbose_name_plural = 'FAQs'
    
    def __str__(self):
        return self.question

class EmailForm(models.Model):
    subject = models.CharField(_('Subject'), max_length=255)
    first_name = models.CharField(_('First Name'), max_length=100)
    last_name = models.CharField(_('Last Name'), max_length=100)
    father_name = models.CharField(_('Father\'s Name'), max_length=100)
    email = models.EmailField(_('Email'))
    phone = models.CharField(_('Phone'), max_length=20)
    region = models.ForeignKey(Region, on_delete=models.CASCADE, verbose_name=_('Region'))
    attachment = models.FileField(
        upload_to='email_attachments/',
        validators=[FileExtensionValidator(['txt', 'doc', 'rtf', 'xls', 'ppt', 'pdf', 'jpg', 'bmp', 'png', 'tiff', 'gif'])],
        max_length=5242880,  # 5MB in bytes
        null=True,
        blank=True,
        verbose_name=_('Attachment')
    )
    message = models.TextField(_('Message'), max_length=5000)
    created_at = models.DateTimeField(_('Created At'), auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Murojaatlar'
        verbose_name_plural = 'Murojaatlar'

    def __str__(self):
        return f'{self.subject} - {self.email}'

class Employee(models.Model):
    WEEKDAY_CHOICES = [
        ('MON', _('Monday')),
        ('TUE', _('Tuesday')),
        ('WED', _('Wednesday')),
        ('THU', _('Thursday')),
        ('FRI', _('Friday')),
        ('SAT', _('Saturday')),
        ('SUN', _('Sunday'))
    ]
    
    fullname = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    working_day = models.CharField(max_length=3, choices=WEEKDAY_CHOICES, default='MON')
    working_hours_start = models.TimeField(help_text='Working hours start time (24-hour format)', default='09:00:00')
    working_hours_end = models.TimeField(help_text='Working hours end time (24-hour format)', default='17:00:00')
    avatar = models.ImageField(upload_to='employees/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['fullname']
        verbose_name = 'Employee'
        verbose_name_plural = 'Employees'
    
    def __str__(self):
        return self.fullname