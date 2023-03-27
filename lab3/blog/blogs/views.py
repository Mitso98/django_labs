from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import viewsets, mixins, permissions, authentication, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination

from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer
from .permissions import IsOwner
# Create your views here.


class PostViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for listing or retrieving users.
    """

    permission_classes = [permissions.IsAuthenticated]
    # serializer_class = PostSerializer
    pagination_class = PageNumberPagination

    def get_queryset(self, pk=None):
        # filter query with date_pub if provided
        # user can only get it's post
        if self.request.resolver_match.kwargs == {}:
            print(">>>>", 'first scope')
            date_published = self.request.query_params.get(
                'date_published', None)
            if date_published is not None:
                queryset = Post.objects.filter(
                    owner=self.request.user, date_pub=date_published)
            else:
                queryset = Post.objects.filter(owner=self.request.user)
        else:
            print(">>>>", 'second scope',
                  self.request.resolver_match.kwargs['pk'])
            pk = self.request.resolver_match.kwargs['pk']
            date_published = self.request.query_params.get(
                'date_published', None)
            if date_published is not None:
                queryset = Post.objects.filter(
                    owner=self.request.user, date_pub=date_published, pk=pk)
            else:
                queryset = Post.objects.filter(owner=self.request.user, pk=pk)

        return queryset

    def list(self, request):
        print("List excuted")
        queryset = self.get_queryset()
        # Paginate the queryset
        paginator = self.pagination_class()
        page = paginator.paginate_queryset(queryset, request)
        serializer = PostSerializer(page, many=True)

        # Create a dictionary with count, next, and previous URLs
        response = {
            'count': paginator.page.paginator.count,
            'next': paginator.get_next_link(),
            'previous': paginator.get_previous_link(),
            'results': serializer.data
        }

        return Response(response)

    def retrieve(self, request, pk=None):
        print("Retrive excuted")
        queryset = self.get_queryset(pk=pk)
        serializer = PostSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        print("Create excuted", request.data)
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response("ok")

    def update(self, request, *args, **kwargs):
        print("Update excuted")
        instance = self.get_object()
        serializer = PostSerializer(instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        print("Delete Request", instance)
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CommentViewSet(viewsets.ModelViewSet):
    
    pagination_class = PageNumberPagination
    
    def get_queryset(self):
        queryset = Comment.objects.filter(post=self.request.resolver_match.kwargs['post_id'])
        return queryset
        
    # list all comments of a specific post
    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        pageinator = self.pagination_class()
        page = pageinator.paginate_queryset(queryset=queryset,request=request)
        serializer = CommentSerializer(page, many=True)
        
        # Create a dictionary with count, next, and previous URLs
        response = {
            'count': pageinator.page.paginator.count,
            'next': pageinator.get_next_link(),
            'previous': pageinator.get_previous_link(),
            'results': serializer.data
        }

        return Response(response)
    
    def retrieve(self, request, *args, **kwargs):
        # get specific post and spcefic comment
        pass