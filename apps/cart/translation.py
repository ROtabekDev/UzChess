from modeltranslation.translator import TranslationOptions, register

from .models import District, PaymentType, Region


@register(Region)
class RegionTranslationOptions(TranslationOptions):
    fields = ("title",)


@register(District)
class DistrictTranslationOptions(TranslationOptions):
    fields = ("title",)


@register(PaymentType)
class PaymentTypeTranslationOptions(TranslationOptions):
    fields = ("title",)
