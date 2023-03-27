from modeltranslation.translator import TranslationOptions, register

from .models import Author, Language, Leval


@register(Leval)
class LevalTranslationOptions(TranslationOptions):
    fields = ("name",)


@register(Author)
class AuthorTranslationOptions(TranslationOptions):
    fields = ("first_name", "last_name")


@register(Language)
class LanguageTranslationOptions(TranslationOptions):
    fields = ("name",)
