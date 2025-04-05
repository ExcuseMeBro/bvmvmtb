from django.db import models
from django.core.validators import FileExtensionValidator
from django.utils.translation import gettext as _
from django.utils.text import slugify
from ckeditor_uploader.fields import RichTextUploadingField
from .translations import MODEL_NAMES, FIELD_NAMES, CHOICES, HELP_TEXTS, ERROR_MESSAGES

class UsefulLink(models.Model):
    name = models.CharField(FIELD_NAMES['name'], max_length=255)
    link = models.URLField(FIELD_NAMES['link'])
    image = models.ImageField(FIELD_NAMES['image'], upload_to='useful_links/')
    created_at = models.DateTimeField(_('Created At'), auto_now_add=True)
    updated_at = models.DateTimeField(_('Updated At'), auto_now=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = MODEL_NAMES['UsefulLink']
        verbose_name_plural = MODEL_NAMES['UsefulLink_plural']

    def __str__(self):
        return self.name

class FilesCategory(models.Model):
    name = models.CharField(FIELD_NAMES['category_name'], max_length=100)
    created_at = models.DateTimeField(_('Created At'), auto_now_add=True)
    updated_at = models.DateTimeField(_('Updated At'), auto_now=True)
    
    class Meta:
        ordering = ['name']
        verbose_name = MODEL_NAMES['FilesCategory']
        verbose_name_plural = MODEL_NAMES['FilesCategory_plural']
    
    def __str__(self):
        return self.name

class Files(models.Model):
    title = models.CharField(FIELD_NAMES['title'], max_length=200)
    description = models.TextField(FIELD_NAMES['description'])
    url = models.URLField(FIELD_NAMES['url'])
    category = models.ForeignKey(FilesCategory, on_delete=models.CASCADE, verbose_name=FIELD_NAMES['category'])
    created_at = models.DateTimeField(_('Created At'), auto_now_add=True)
    updated_at = models.DateTimeField(_('Updated At'), auto_now=True)
    
    class Meta:
        ordering = ['-created_at']
        verbose_name = MODEL_NAMES['Files']
        verbose_name_plural = MODEL_NAMES['Files_plural']
    
    def __str__(self):
        return self.title

class Region(models.Model):
    name = models.CharField(FIELD_NAMES['region_name'], max_length=100)
    code = models.CharField(FIELD_NAMES['code'], max_length=10, unique=True, help_text=HELP_TEXTS['region_code'])
    is_active = models.BooleanField(FIELD_NAMES['is_active'], default=True)
    created_at = models.DateTimeField(_('Created At'), auto_now_add=True)
    updated_at = models.DateTimeField(_('Updated At'), auto_now=True)
    
    class Meta:
        ordering = ['name']
        verbose_name = MODEL_NAMES['Region']
        verbose_name_plural = MODEL_NAMES['Region_plural']
    
    def __str__(self):
        return self.name

class City(models.Model):
    name = models.CharField(FIELD_NAMES['city_name'], max_length=100)
    region = models.ForeignKey(Region, on_delete=models.CASCADE, related_name='cities', verbose_name=FIELD_NAMES['region'])
    is_active = models.BooleanField(FIELD_NAMES['is_active'], default=True)
    created_at = models.DateTimeField(_('Created At'), auto_now_add=True)
    updated_at = models.DateTimeField(_('Updated At'), auto_now=True)
    
    class Meta:
        ordering = ['name']
        verbose_name = MODEL_NAMES['City']
        verbose_name_plural = MODEL_NAMES['City_plural']
    
    def __str__(self):
        return self.name

class FAQ(models.Model):
    question = models.CharField(FIELD_NAMES['question'], max_length=200)
    answer = models.TextField(FIELD_NAMES['answer'])
    order = models.IntegerField(FIELD_NAMES['order'], default=0)
    created_at = models.DateTimeField(_('Created At'), auto_now_add=True)
    updated_at = models.DateTimeField(_('Updated At'), auto_now=True)
    
    class Meta:
        ordering = ['order', '-created_at']
        verbose_name = MODEL_NAMES['FAQ']
        verbose_name_plural = MODEL_NAMES['FAQ_plural']
    
    def __str__(self):
        return self.question

class EmailForm(models.Model):
    subject = models.CharField(FIELD_NAMES['subject'], max_length=255)
    first_name = models.CharField(FIELD_NAMES['first_name'], max_length=100)
    last_name = models.CharField(FIELD_NAMES['last_name'], max_length=100)
    father_name = models.CharField(FIELD_NAMES['father_name'], max_length=100)
    email = models.EmailField(FIELD_NAMES['email'])
    phone = models.CharField(FIELD_NAMES['phone'], max_length=20)
    region = models.ForeignKey(Region, on_delete=models.CASCADE, verbose_name=FIELD_NAMES['region'])
    attachment = models.FileField(
        upload_to='email_attachments/',
        validators=[FileExtensionValidator(['txt', 'doc', 'rtf', 'xls', 'ppt', 'pdf', 'jpg', 'bmp', 'png', 'tiff', 'gif'])],
        max_length=5242880,  # 5MB in bytes
        null=True,
        blank=True,
        verbose_name=FIELD_NAMES['attachment']
    )
    message = models.TextField(FIELD_NAMES['message'], max_length=5000)
    created_at = models.DateTimeField(_('Created At'), auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = MODEL_NAMES['EmailForm']
        verbose_name_plural = MODEL_NAMES['EmailForm_plural']

    def __str__(self):
        return f'{self.subject} - {self.email}'

class Employee(models.Model):
    WEEKDAY_CHOICES = CHOICES['WEEKDAY_CHOICES']
    
    fullname = models.CharField(FIELD_NAMES['fullname'], max_length=100)
    position = models.CharField(FIELD_NAMES['position'], max_length=100)
    working_day = models.CharField(FIELD_NAMES['working_day'], max_length=3, choices=WEEKDAY_CHOICES, default='MON')
    working_hours_start = models.TimeField(help_text=HELP_TEXTS['working_hours_start'], default='09:00:00')
    working_hours_end = models.TimeField(help_text=HELP_TEXTS['working_hours_end'], default='17:00:00')
    avatar = models.ImageField(FIELD_NAMES['avatar'], upload_to='employees/', null=True, blank=True)
    created_at = models.DateTimeField(_('Created At'), auto_now_add=True)
    updated_at = models.DateTimeField(_('Updated At'), auto_now=True)
    
    class Meta:
        ordering = ['fullname']
        verbose_name = MODEL_NAMES['Employee']
        verbose_name_plural = MODEL_NAMES['Employee_plural']
    
    def __str__(self):
        return self.fullname

class NewsType(models.Model):
    name = models.CharField(FIELD_NAMES['news_type_name'], max_length=100)
    created_at = models.DateTimeField(_('Created At'), auto_now_add=True)
    updated_at = models.DateTimeField(_('Updated At'), auto_now=True)
    
    class Meta:
        ordering = ['name']
        verbose_name = MODEL_NAMES['NewsType']
        verbose_name_plural = MODEL_NAMES['NewsType_plural']
    
    def __str__(self):
        return self.name

class News(models.Model):
    title = models.CharField(FIELD_NAMES['news_title'], max_length=200)
    image = models.ImageField(FIELD_NAMES['news_image'], upload_to='news/')
    news_type = models.ForeignKey(NewsType, on_delete=models.CASCADE, verbose_name=FIELD_NAMES['news_type'])
    description = RichTextUploadingField(FIELD_NAMES['news_description'])
    hashtag = models.CharField(FIELD_NAMES['hashtag'], max_length=100)
    created_at = models.DateTimeField(_('Created At'), auto_now_add=True)
    updated_at = models.DateTimeField(_('Updated At'), auto_now=True)
    
    class Meta:
        ordering = ['-created_at']
        verbose_name = MODEL_NAMES['News']
        verbose_name_plural = MODEL_NAMES['News_plural']
    
    def __str__(self):
        return self.title

class Statistics(models.Model):
    name = models.CharField(FIELD_NAMES['statistics_name'], max_length=100)
    quantity = models.IntegerField(FIELD_NAMES['quantity'], default=0)
    created_at = models.DateTimeField(_('Created At'), auto_now_add=True)
    updated_at = models.DateTimeField(_('Updated At'), auto_now=True)
    
    class Meta:
        ordering = ['name']
        verbose_name = MODEL_NAMES['Statistics']
        verbose_name_plural = MODEL_NAMES['Statistics_plural']
    
    def __str__(self):
        return self.name

class Offer(models.Model):
    CATEGORY_CHOICES = CHOICES['CATEGORY_CHOICES']
    
    fullname = models.CharField(FIELD_NAMES['offer_fullname'], max_length=100)
    region = models.ForeignKey(Region, on_delete=models.CASCADE, verbose_name=FIELD_NAMES['offer_region'])
    city = models.ForeignKey(City, on_delete=models.CASCADE, verbose_name=FIELD_NAMES['offer_city'])
    phone = models.CharField(FIELD_NAMES['offer_phone'], max_length=20)
    category = models.CharField(FIELD_NAMES['offer_category'], max_length=20, choices=CATEGORY_CHOICES)
    message = models.TextField(FIELD_NAMES['offer_message'], max_length=1000)
    created_at = models.DateTimeField(_('Created At'), auto_now_add=True)
    updated_at = models.DateTimeField(_('Updated At'), auto_now=True)
    
    class Meta:
        ordering = ['-created_at']
        verbose_name = MODEL_NAMES['Offer']
        verbose_name_plural = MODEL_NAMES['Offer_plural']
    
    def __str__(self):
        return f'{self.fullname} - {self.get_category_display()}'

class OfferStats(models.Model):
    name = models.CharField(FIELD_NAMES['offer_stats_name'], max_length=100)
    quantity = models.IntegerField(FIELD_NAMES['offer_stats_quantity'], default=0)
    created_at = models.DateTimeField(_('Created At'), auto_now_add=True)
    updated_at = models.DateTimeField(_('Updated At'), auto_now=True)

    class Meta:
        ordering = ['name']
        verbose_name = MODEL_NAMES['OfferStats']
        verbose_name_plural = MODEL_NAMES['OfferStats_plural']

    def __str__(self):
        return self.name

class PersonType(models.Model):
    name = models.CharField(FIELD_NAMES['person_type_name'], max_length=100)
    created_at = models.DateTimeField(_('Created At'), auto_now_add=True)
    updated_at = models.DateTimeField(_('Updated At'), auto_now=True)

    class Meta:
        ordering = ['name']
        verbose_name = MODEL_NAMES['PersonType']
        verbose_name_plural = MODEL_NAMES['PersonType_plural']

    def __str__(self):
        return self.name

class Persons(models.Model):
    position = models.CharField(FIELD_NAMES['person_position'], max_length=200)
    biography = models.TextField(FIELD_NAMES['biography'])
    start_hour = models.TimeField(FIELD_NAMES['start_hour'])
    end_hour = models.TimeField(FIELD_NAMES['end_hour'])
    phone = models.CharField(FIELD_NAMES['person_phone'], max_length=20)
    email = models.EmailField(FIELD_NAMES['person_email'])
    telegram = models.URLField(FIELD_NAMES['telegram'], blank=True, null=True)
    work_experience = models.TextField(FIELD_NAMES['work_experience'])
    responsibilities = models.TextField(FIELD_NAMES['responsibilities'])
    type = models.ForeignKey(
        PersonType,
        on_delete=models.CASCADE,
        verbose_name=FIELD_NAMES['person_type'],
        related_name='persons'
    )
    created_at = models.DateTimeField(_('Created At'), auto_now_add=True)
    updated_at = models.DateTimeField(_('Updated At'), auto_now=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = MODEL_NAMES['Persons']
        verbose_name_plural = MODEL_NAMES['Persons_plural']

    def __str__(self):
        return self.position

class Gallery(models.Model):
    CONTENT_TYPE_CHOICES = CHOICES['CONTENT_TYPE_CHOICES']
    
    title = models.CharField(FIELD_NAMES['gallery_title'], max_length=200)
    description = models.TextField(FIELD_NAMES['gallery_description'], blank=True, null=True)
    content_type = models.CharField(
        FIELD_NAMES['content_type'],
        max_length=10,
        choices=CONTENT_TYPE_CHOICES,
        default='photo'
    )
    image = models.ImageField(
        FIELD_NAMES['gallery_image'],
        upload_to='gallery/photos/',
        blank=True,
        null=True,
        help_text=HELP_TEXTS['gallery_image']
    )
    video_url = models.URLField(
        FIELD_NAMES['video_url'],
        blank=True,
        null=True,
        help_text=HELP_TEXTS['video_url']
    )
    created_at = models.DateTimeField(_('Created At'), auto_now_add=True)
    updated_at = models.DateTimeField(_('Updated At'), auto_now=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = MODEL_NAMES['Gallery']
        verbose_name_plural = MODEL_NAMES['Gallery_plural']
        indexes = [
            models.Index(fields=['content_type']),
        ]

    def __str__(self):
        return self.title

    def clean(self):
        from django.core.exceptions import ValidationError
        if self.content_type == 'photo' and not self.image:
            raise ValidationError(ERROR_MESSAGES['gallery_photo_required'])
        if self.content_type == 'video' and not self.video_url:
            raise ValidationError(ERROR_MESSAGES['gallery_video_required'])