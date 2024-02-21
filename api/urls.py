from django.urls import path
from .views import GalleryList

urlpatterns = [
    path('item/', GalleryList.as_view()),
]
