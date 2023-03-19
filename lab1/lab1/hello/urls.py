from django.urls import path
from . import views
urlpatterns = [
    path('hello/<name>', views.hello_random),
    
]