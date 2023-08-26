from modeltranslation.translator import register, TranslationOptions
from .models import (
    Weeks, Treiner
)

@register(Treiner)
class TrainerOptions(TranslationOptions):
    fields = ("f_name", "professional", "about")


@register(Weeks)
class WeeksOptions(TranslationOptions):
    fields = ("name", )