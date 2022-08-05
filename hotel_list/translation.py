from modeltranslation.translator import register, TranslationOptions
from .models import Rooms, News, Reviews, NewsReviews, Services, NewsShots


@register(Rooms)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name', 'bed', 'description')


@register(News)
class ActorTranslationOptions(TranslationOptions):
    fields = ('name', 'text_state', 'date')


@register(Reviews)
class GenreTranslationOptions(TranslationOptions):
    fields = ('name', 'text', 'room', 'date')


@register(NewsReviews)
class MovieTranslationOptions(TranslationOptions):
    fields = ('name', 'text', 'news', 'date')


@register(Services)
class MovieShotsTranslationOptions(TranslationOptions):
    fields = ('name',)


@register(NewsShots)
class MovieShotsTranslationOptions(TranslationOptions):
    fields = ('title', 'description')