from django.urls import path
from . import views


urlpatterns = [
    path('about-us',views.about_us,name='aboutus'),
    path('contact-us',views.contact_us,name='contact'),
    ]