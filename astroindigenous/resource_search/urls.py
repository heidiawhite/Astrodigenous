from django.urls import path
from .views import home, search

urlpatterns = [
    path('q', search),
    path('', home)
]
