import datetime
from django import forms
from .models import Reviews, NewsReviews, RatingStar, Rating
from bootstrap_datepicker_plus import DateTimePickerInput
from django import forms
from django.core.mail import send_mail


class ReviewForm(forms.ModelForm):
    """Форма отзывов"""
    class Meta:
        model = Reviews
        fields = ("name", "email", "text")


class NewsReviewForm(forms.ModelForm):
    """Форма отзывов"""
    class Meta:
        model = NewsReviews
        fields = ("name", "email", "text")


class ContactForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    message = forms.CharField(widget = forms.Textarea)



class RatingForm(forms.ModelForm):
    """Форма добавления рейтинга"""
    star = forms.ModelChoiceField(
        queryset=RatingStar.objects.all(), widget=forms.RadioSelect(), empty_label=None
    )

    class Meta:
        model = Rating
        fields = ("star",)

