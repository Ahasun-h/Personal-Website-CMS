# Import Librarys
from django.urls import path
from . import views 

from django.conf.urls.static import static
from django.conf import Settings, settings


# Urls
urlpatterns = [
    path('',views.index,name='index'),
    path('about/',views.about,name='about'),
    path('resume/',views.resume,name='resume'),
    path('portfolio/',views.portfolio,name='portfolio'),
    path('blog/',views.blog,name='blog'),

    path('blog-single/<slug:slug>/',views.post_details, name='post_details'),

    path('contact/',views.contact,name='contact'),
    path('send_mail/', views.send_gmail, name="send_mail"),

]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)