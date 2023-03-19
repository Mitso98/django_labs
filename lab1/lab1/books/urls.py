from django.urls import path
from . import views
urlpatterns = [
    path('books/<int:book_id>', views.book),
]
