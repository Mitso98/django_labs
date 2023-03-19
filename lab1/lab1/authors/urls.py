from django.urls import path
from . import views
urlpatterns = [
    path('authors', views.authors),
    path('authors/<int:author_id>', views.author),
]
