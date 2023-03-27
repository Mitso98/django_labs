from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import PostViewSet, CommentViewSet

# app_name = 'blogs'
# router = DefaultRouter()

# router.register('post', PostViewSet, basename='post')
# # router.register('comment', CommentViewSet, basename='comment')
# urlpatterns = router.urls


urlpatterns = [
    path('posts/<int:pk>', PostViewSet.as_view(
        {'delete': 'destroy', 'get': 'retrieve', 'put': 'update', 'patch': 'update'})),
    path('posts', PostViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('comments/<int:post_id>', CommentViewSet.as_view({'get': 'list'})),
    
]
