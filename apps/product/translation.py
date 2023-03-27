from modeltranslation.translator import TranslationOptions, register

from .models import FeatureName, Product


@register(Product)
class ProductTranslationOptions(TranslationOptions):
    fields = ("title", "description")


@register(FeatureName)
class FeatureNameTranslationOptions(TranslationOptions):
    fields = ("title",)
