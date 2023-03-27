from modeltranslation.translator import TranslationOptions, register

from .models import Book, CategoryForCourse, Course, Episode, Section


@register(CategoryForCourse)
class CategoryForCourseTranslationOptions(TranslationOptions):
    fields = ("title",)


@register(Course)
class CourseTranslationOptions(TranslationOptions):
    fields = ("title", "desciption")


@register(Section)
class SectionTranslationOptions(TranslationOptions):
    fields = ("title",)


@register(Episode)
class EpisodeTranslationOptions(TranslationOptions):
    fields = ("title",)


@register(Book)
class BookTranslationOptions(TranslationOptions):
    fields = ("title", "desciption")
