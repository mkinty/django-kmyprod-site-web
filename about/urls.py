from django.urls import path
from . import views


urlpatterns = [
    # post views

    path('services', views.services_detail, name='services'),
    path('instructors', views.instructors_detail, name='instructors'),
    path('projets', views.projets_detail, name='projets'),
    path('contact', views.contact_detail, name='contact'),
]
