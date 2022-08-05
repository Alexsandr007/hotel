from django.db import models

from django.urls import reverse
from django.core.validators import RegexValidator, MaxValueValidator
from taggit.managers import TaggableManager


class Services(models.Model):
    name = models.CharField("Имя сервиса", max_length = 150)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Сервис"
        verbose_name_plural = "Сервисы"


class Rooms(models.Model):
    name = models.CharField("Имя", max_length = 150)
    cost = models.IntegerField("Цена", default = 0, help_text = "указывать сумму в долларах")
    size = models.PositiveSmallIntegerField("Размер номера", help_text = "указывать размер в футах")
    capacity = models.PositiveSmallIntegerField("Кол-во персон", )
    bed = models.CharField("Краткое описание спального места", max_length = 150 )
    services = models.ManyToManyField(Services)
    description = models.TextField("Описание")
    img = models.ImageField("Фотография комнаты", upload_to = "Rooms_shots/")
    url = models.SlugField(max_length = 130, unique = True)
    reservaton = models.BooleanField("Резервация")


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Комната"
        verbose_name_plural = "Комнаты"

    def get_absolute_url(self):
        return reverse("rooms_detail", kwargs = {"slug": self.url})

    def get_review(self):
        return self.reviews_set.all()



class RatingStar(models.Model):
    """Звезда рейтинга"""
    value = models.SmallIntegerField("Значение", default=0)

    def __str__(self):
        return f'{self.value}'

    class Meta:
        verbose_name = "Звезда рейтинга"
        verbose_name_plural = "Звезды рейтинга"
        ordering = ["value"]


class Rating(models.Model):
    """Рейтинг"""
    ip = models.CharField("IP адрес", max_length=15)
    star = models.ForeignKey(RatingStar, on_delete=models.CASCADE, verbose_name="звезда")
    rooms = models.ForeignKey(Rooms, on_delete=models.CASCADE, verbose_name="комната")

    def __str__(self):
        return f"{self.star} - {self.rooms}"

    class Meta:
        verbose_name = "Рейтинг"
        verbose_name_plural = "Рейтинги"


class Reviews(models.Model):
    """Отзывы для комнат"""
    email = models.EmailField()
    name = models.CharField("Имя", max_length=100)
    text = models.TextField("Сообщение", max_length=5000)
    room = models.ForeignKey(Rooms, verbose_name="комната", on_delete=models.CASCADE)
    date = models.DateField("Дата")
    parent = models.ForeignKey('self', verbose_name = "Родитель", on_delete = models.SET_NULL, blank = True, null = True)

    def __str__(self):
        return f"{self.name} - {self.room}"

    class Meta:
        verbose_name = "Отзыв к комнате"
        verbose_name_plural = "Отзывы к комнатам"

class News(models.Model):
    """Новости"""
    name = models.CharField("Имя", max_length=150)
    text_state = models.TextField("Текст статьи")
    date = models.DateField("Дата")
    author = models.EmailField("email автора")
    image = models.ImageField("Фотография", upload_to="News_shots/",)
    url = models.SlugField(max_length=130, unique=True)
    # tags = TaggableManager()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("news_detail", kwargs={"slug": self.url})

    def get_review(self):
        return self.newsreviews_set.filter(parent__isnull=True)

    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"


class NewsShots(models.Model):
    """Фотографии к новостям"""
    title = models.CharField("Название", max_length=150)
    description = models.TextField("Описание")
    image = models.ImageField("Изображение", upload_to = "movie_shots/")
    news = models.ForeignKey(News, verbose_name = "Новость", on_delete = models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Фотографии для новости"
        verbose_name_plural = "Фотографии для новостей"


class NewsReviews(models.Model):
    """Отзывы для новостей"""
    email = models.EmailField()
    name = models.CharField("Имя", max_length = 100)
    text = models.TextField("Сообщение", max_length = 5000)
    news = models.ForeignKey(News, verbose_name="фильм", on_delete = models.CASCADE)
    date = models.DateField("Дата")
    parent = models.ForeignKey('self', verbose_name = "Родитель", on_delete = models.SET_NULL, blank = True, null = True)

    def __str__(self):
        return f"{self.name} - {self.news}"

    class Meta:
        verbose_name = "Отзыв к новости"
        verbose_name_plural = "Отзывы к новостям"

