from django.urls import path, include

from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
    path("rooms/", views.RoomsView.as_view(), name="rooms"),
    path("rooms/<slug:slug>/", views.RoomsDetailView.as_view(), name="rooms_detail"),
    path("about_us/", views.AboutUsView.as_view(), name="about_us"),
    path("news/", views.NewsView.as_view(), name="news"),
    path("news/<slug:slug>/", views.NewsDetailView.as_view(), name="news_detail"),
    path("room_review/<int:pk>/", views.AddReviewRoom.as_view(), name="room_add_review"),
    path("news_review/<int:pk>/", views.AddReviewNews.as_view(), name="news_add_review"),
    path("contact/", views.ContactFormView.as_view(), name="contact"),
    path("contact/send/email/", views.ContactFormView.send, name="contact_send_email"),
    path("contact_room/<slug:slug>/", views.ContactFormView.form, name="contact_room"),
    path("contact/send/", views.ContactFormView.reservation_room, name="reserve_a_room"),
    path("add-rating/", views.AddStarRating.as_view(), name='add_rating'),
    path('ckeditor/', include('ckeditor_uploader.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)