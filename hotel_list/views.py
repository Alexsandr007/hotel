import datetime
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.base import View
from django.views.generic.edit import FormView
from .tasks import send_message
from validate_email import validate_email
from .models import *
from .forms import ReviewForm, NewsReviewForm, ContactForm, RatingForm
from taggit.models import Tag
from django.core.paginator import Paginator


class HomeView(View):
    """Начальная страница"""
    def get(self, request):
        rooms = Rooms.objects.all()
        news = News.objects.all()

        return render(request, "index.html", {'rooms': rooms, 'news': news})


class RoomsView(ListView):
    """Список комнат"""
    paginate_by = 1
    model = Rooms
    queryset = Rooms.objects.filter(reservaton=False)
    ordering = ['cost']
    template_name = "rooms.html"



class RoomsDetailView(DetailView):
    """Полное описание комнаты"""
    model = Rooms
    slug_field = "url"
    template_name = "room_details.html"

    def get_rating(self, slug):
        room = Rooms.objects.get(id=1)
        print(room)
        queryset = Rating.objects.all(rooms=room[1].id)
        print(queryset)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        slug = self.slug_field
        context["star_form"] = RatingForm()
        #context["rating"] = self.get_rating(slug)
        return context




class AboutUsView(View):
    """Начальная страница"""
    def get(self, request):

        return render(request, "about-us.html")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["rooms"] = Rooms.objects.all()[:4]
        return context


class NewsView(ListView):
    """Список комнат"""
    paginate_by = 1
    model = News
    queryset = News.objects.all()
    ordering = ['-id']
    template_name = "news.html"


class NewsDetailView(DetailView):
    """Полное описание комнаты"""
    model = News
    slug_field = "url"
    template_name = "news_details.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["recommend_news"] = News.objects.all()[:3]
        return context



class AddReviewRoom(View):
    """Отзывы"""

    def post(self, request, pk):
        form = ReviewForm(request.POST)
        room = Rooms.objects.get(id=pk)
        if form.is_valid():
            form = form.save(commit=False)
            form.date = datetime.datetime.now()
            if request.POST.get("parent", None):
                form.parent_id = int(request.POST.get("parent"))
            form.room = room
            form.save()

        return redirect(room.get_absolute_url())

class AddReviewNews(View):
    """Отзывы"""

    def post(self, request, pk):
        form = NewsReviewForm(request.POST)
        news = News.objects.get(id=pk)
        if form.is_valid():
            form = form.save(commit=False)
            form.date = datetime.datetime.now()
            if request.POST.get("parent", None):
                form.parent_id = int(request.POST.get("parent"))
            form.news = news
            form.save()

        return redirect(news.get_absolute_url())


class ContactFormView(FormView):
    template_name = 'contact.html'
    form_class = ContactForm
    success_url = '/contact/'

    def send(request):
        """ Send message """
        if request.method == 'POST':
            email_form = request.POST
            send_message.delay(email_form['name'], email_form['message'], email_form['email'])
        return redirect('contact')

    def form(request, slug):
        queryset = Rooms.objects.get(url=slug)
        return render(request, "contact_room.html",{"queryset" : queryset})

    def reservation_room(request):
        """ Send message """
        if request.method == 'POST':
            email_form = request.POST
            is_valid = validate_email(email_form['email'])
            if is_valid == True:
                send_message.delay(email_form['name'], email_form['message'], email_form['email'], email_form['slug'])
        return redirect('contact')

class AddStarRating(View):

    def get_client_ip(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip

    def post(self, request):
        form = RatingForm(request.POST)
        if form.is_valid():
            Rating.objects.update_or_create(
                ip=self.get_client_ip(request),
                rooms_id=request.POST.get("rooms"),
                defaults={'star_id': int(request.POST.get("star"))}
            )
            return HttpResponse(status=201)
        else:
            return HttpResponse(status=400)

