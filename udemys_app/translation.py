from .models import (Category, SubCategory, Level, Course,
                     Lesson, AssignMent, Exam, Questions,
                     Option, Review)
from modeltranslation.translator import TranslationOptions,register

@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('category_name', )


@register(SubCategory)
class SubCategoryTranslationOptions(TranslationOptions):
    fields = ('subcategory_name', )


@register(Level)
class LevelTranslationOptions(TranslationOptions):
    fields = ('level', )


@register(Course)
class CourseTranslationOptions(TranslationOptions):
    fields = ('course_name', 'description')


@register(Lesson)
class LessonTranslationOptions(TranslationOptions):
    fields = ('title', )


@register(AssignMent)
class AssignMentTranslationOptions(TranslationOptions):
    fields = ('title', 'description')


@register(Exam)
class LessonTranslationOptions(TranslationOptions):
    fields = ('title', )


@register(Questions)
class QuestionsTranslationOptions(TranslationOptions):
    fields = ('question_name', )


@register(Option)
class OptionTranslationOptions(TranslationOptions):
    fields = ('option_name', )


@register(Review)
class LessonTranslationOptions(TranslationOptions):
    fields = ('comment', )