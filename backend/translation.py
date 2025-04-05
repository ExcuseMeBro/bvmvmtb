from modeltranslation.translator import register, TranslationOptions
from .models import (
    FAQ, UsefulLink, FilesCategory, Files, Region, City, 
    EmailForm, Employee, NewsType, News, 
    Statistics, Offer, OfferStats, PersonType, Persons, Gallery
)

@register(UsefulLink)
class UsefulLinkTranslationOptions(TranslationOptions):
    fields = ('name',)

@register(FilesCategory)
class FilesCategoryTranslationOptions(TranslationOptions):
    fields = ('name',)

@register(Files)
class FilesTranslationOptions(TranslationOptions):
    fields = ('title', 'description')

@register(Region)
class RegionTranslationOptions(TranslationOptions):
    fields = ('name',)

@register(City)
class CityTranslationOptions(TranslationOptions):
    fields = ('name',)

@register(FAQ)
class FAQTranslationOptions(TranslationOptions):
    fields = ('question', 'answer')

@register(EmailForm)
class EmailFormTranslationOptions(TranslationOptions):
    fields = ('subject', 'message')

@register(Employee)
class EmployeeTranslationOptions(TranslationOptions):
    fields = ('fullname', 'position')

@register(NewsType)
class NewsTypeTranslationOptions(TranslationOptions):
    fields = ('name',)

@register(News)
class NewsTranslationOptions(TranslationOptions):
    fields = ('title', 'description', 'hashtag')

@register(Statistics)
class StatisticsTranslationOptions(TranslationOptions):
    fields = ('name',)

@register(Offer)
class OfferTranslationOptions(TranslationOptions):
    fields = ('fullname', 'message')

@register(OfferStats)
class OfferStatsTranslationOptions(TranslationOptions):
    fields = ('name',)

@register(PersonType)
class PersonTypeTranslationOptions(TranslationOptions):
    fields = ('name',)

@register(Persons)
class PersonsTranslationOptions(TranslationOptions):
    fields = ('position', 'biography', 'work_experience', 'responsibilities')

@register(Gallery)
class GalleryTranslationOptions(TranslationOptions):
    fields = ('title', 'description')