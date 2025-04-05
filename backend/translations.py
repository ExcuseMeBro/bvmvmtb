from django.utils.translation import gettext_lazy as _

# Model Names
MODEL_NAMES = {
    'UsefulLink': _('Foydali havola'),
    'UsefulLink_plural': _('Foydali havolalar'),
    'FilesCategory': _('Fayllar kategoriyasi'),
    'FilesCategory_plural': _('Fayllar kategoriyalari'),
    'Files': _('Fayl'),
    'Files_plural': _('Fayllar'),
    'Region': _('Viloyat'),
    'Region_plural': _('Viloyatlar'),
    'City': _('Tuman'),
    'City_plural': _('Tumanlar'),
    'FAQ': _('Ko\'p so\'raladigan savollar'),
    'FAQ_plural': _('Ko\'p so\'raladigan savollar'),
    'EmailForm': _('Murojaatlar'),
    'EmailForm_plural': _('Murojaatlar'),
    'Employee': _('Xodim'),
    'Employee_plural': _('Xodimlar'),
    'NewsType': _('Yangiliklar turi'),
    'NewsType_plural': _('Yangiliklar turlari'),
    'NewsCategory': _('Yangiliklar kategoriyasi'),
    'NewsCategory_plural': _('Yangiliklar kategoriyalari'),
    'News': _('Yangilik'),
    'News_plural': _('Yangiliklar'),
    'Statistics': _('Statistika'),
    'Statistics_plural': _('Statistika'),
    'Offer': _('Taklif'),
    'Offer_plural': _('Takliflar'),
    'OfferStats': _('Takliflar statistikasi'),
    'OfferStats_plural': _('Takliflar statistikasi'),
    'PersonType': _('Shaxs turi'),
    'PersonType_plural': _('Shaxs turlari'),
    'Persons': _('Shaxs'),
    'Persons_plural': _('Shaxslar'),
    'Gallery': _('Galereya'),
    'Gallery_plural': _('Galereya'),
}

# Field Names
FIELD_NAMES = {
    # UsefulLink
    'name': _('Nomi'),
    'link': _('Havola'),
    'image': _('Rasm'),
    
    # FilesCategory
    'category_name': _('Kategoriya nomi'),
    
    # Files
    'title': _('Sarlavha'),
    'description': _('Tavsif'),
    'url': _('URL'),
    'category': _('Kategoriya'),
    
    # Region
    'region_name': _('Viloyat nomi'),
    'code': _('Kod'),
    'is_active': _('Faol'),
    
    # City
    'city_name': _('Tuman nomi'),
    'region': _('Viloyat'),
    
    # FAQ
    'question': _('Savol'),
    'answer': _('Javob'),
    'order': _('Tartib'),
    
    # EmailForm
    'subject': _('Mavzu'),
    'first_name': _('Ism'),
    'last_name': _('Familiya'),
    'father_name': _('Otasining ismi'),
    'email': _('Email'),
    'phone': _('Telefon'),
    'attachment': _('Ilova'),
    'message': _('Xabar'),
    
    # Employee
    'fullname': _('To\'liq ism'),
    'position': _('Lavozim'),
    'working_day': _('Ish kuni'),
    'working_hours_start': _('Ish vaqtining boshlanishi'),
    'working_hours_end': _('Ish vaqtining tugashi'),
    'avatar': _('Rasm'),
    
    # NewsType
    'news_type_name': _('Yangilik turi'),
    
    # NewsCategory
    'news_category_name': _('Yangiliklar kategoriyasi'),
    
    # News
    'news_title': _('Yangilik sarlavhasi'),
    'news_image': _('Yangilik rasmi'),
    'news_type': _('Yangilik turi'),
    'news_category': _('Yangiliklar kategoriyasi'),
    'news_description': _('Yangilik tavsifi'),
    'hashtag': _('Xeshteg'),
    
    # Statistics
    'statistics_name': _('Statistika nomi'),
    'quantity': _('Soni'),
    
    # Offer
    'offer_fullname': _('To\'liq ism'),
    'offer_region': _('Viloyat'),
    'offer_city': _('Tuman'),
    'offer_phone': _('Telefon'),
    'offer_category': _('Kategoriya'),
    'offer_message': _('Xabar'),
    
    # OfferStats
    'offer_stats_name': _('Takliflar statistikasi nomi'),
    'offer_stats_quantity': _('Takliflar soni'),
    
    # PersonType
    'person_type_name': _('Shaxs turi nomi'),
    
    # Persons
    'person_position': _('Lavozim'),
    'biography': _('Biografiya'),
    'start_hour': _('Qabul vaqtining boshlanishi'),
    'end_hour': _('Qabul vaqtining tugashi'),
    'person_phone': _('Telefon'),
    'person_email': _('Email'),
    'telegram': _('Telegram sahifasi'),
    'work_experience': _('Mehnat faoliyati'),
    'responsibilities': _('Vazifalar'),
    'person_type': _('Shaxs turi'),
    
    # Gallery
    'gallery_title': _('Galereya sarlavhasi'),
    'gallery_description': _('Galereya tavsifi'),
    'content_type': _('Kontent turi'),
    'gallery_image': _('Galereya rasmi'),
    'video_url': _('Video URL'),
}

# Choices
CHOICES = {
    'WEEKDAY_CHOICES': [
        ('MON', _('Dushanba')),
        ('TUE', _('Seshanba')),
        ('WED', _('Chorshanba')),
        ('THU', _('Payshanba')),
        ('FRI', _('Juma')),
        ('SAT', _('Shanba')),
        ('SUN', _('Yakshanba'))
    ],
    'CATEGORY_CHOICES': [
        ('preschool', _('Maktabgacha ta\'lim')),
        ('school', _('Maktab ta\'limi'))
    ],
    'CONTENT_TYPE_CHOICES': [
        ('photo', _('Rasm')),
        ('video', _('Video')),
    ],
}

# Help Texts
HELP_TEXTS = {
    'working_hours_start': _('Ish vaqtining boshlanishi (24 soatlik format)'),
    'working_hours_end': _('Ish vaqtining tugashi (24 soatlik format)'),
    'region_code': _('Viloyat uchun noyob identifikator'),
    'gallery_image': _('Faqat rasmlar uchun'),
    'video_url': _('Faqat videolar uchun'),
}

# Error Messages
ERROR_MESSAGES = {
    'gallery_photo_required': _('Rasm yuklanishi shart'),
    'gallery_video_required': _('Video URL kiritilishi shart'),
} 