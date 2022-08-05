from django.contrib import admin
from .models import *
from ckeditor.widgets import CKEditorWidget
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from modeltranslation.admin import TranslationAdmin
from django import forms




class NewsAdminForm(forms.ModelForm):
    """Форма с виджетом ckeditor"""
    text_state_ru = forms.CharField(label="Описание ru", widget=CKEditorUploadingWidget())
    text_state_en = forms.CharField(label="Описание en", widget=CKEditorUploadingWidget())

    class Meta:
        model = News
        fields = '__all__'

@admin.register(Rooms)
class RoomsAdmin(TranslationAdmin):
    """Комнаты"""
    search_fields = ('name', 'description',)
    list_filter = ('cost', 'capacity', )


@admin.register(News)
class NewsAdmin(TranslationAdmin):
    form = NewsAdminForm
    list_display = ("name", "date",)
    search_fields = ('name', 'text_state',)
    list_filter = ('date',)

@admin.register(Services)
class ServicesAdmin(TranslationAdmin):
    list_display = ("name" , )

@admin.register(Reviews)
class ServicesAdmin(TranslationAdmin):
    list_display = ("name" , "room", "date")


@admin.register(NewsReviews)
class ServicesAdmin(TranslationAdmin):
    list_display = ("name" , "news", "date")

@admin.register(NewsShots)
class ServicesAdmin(TranslationAdmin):
    list_display = ("title" , "description", )



admin.site.register(RatingStar)
admin.site.register(Rating)


