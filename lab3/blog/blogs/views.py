from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import viewsets, filters, permissions, authentication, status
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
    serializer_class = PostSerializer
    pagination_class = PageNumberPagination
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'date_pub']

    def get_queryset(self, pk=None):
        # TODO: refactor this method as we are using filter API
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
        queryset = self.filter_queryset(self.get_queryset())
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
        queryset = self.get_queryset(pk=pk)
        serializer = PostSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

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
    serializer_class = CommentSerializer

    def authorization(self, request, instance):
        # authorization
        if instance.owner.id == request.user.id:
            return True
        else:
            return False

    def get_queryset(self):
        queryset = Comment.objects.filter(
            post=self.request.resolver_match.kwargs['post_id'])
        return queryset

    # list all comments of a specific post
    def list(self, request, *args, **kwargs):
        print("comments\list")
        queryset = self.get_queryset()
        pageinator = self.pagination_class()
        page = pageinator.paginate_queryset(queryset=queryset, request=request)
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
        # get spcefic comment
        # url /comments/comment_id
        print('comments/retrive')
        comment_id = self.request.resolver_match.kwargs['comment_id']

        queryset = get_object_or_404(Comment, id=comment_id)
        serializer = self.serializer_class(queryset)

        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        print('Comments/create')
        seralizer = self.serializer_class(data=request.data)
        if seralizer.is_valid():
            seralizer.save()
            return Response(seralizer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(seralizer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        # url /comments/update/comment_id
        print("comments/update")
        comment_id = self.request.resolver_match.kwargs['comment_id']
        instance = get_object_or_404(Comment, id=comment_id)
        serializer = self.serializer_class(instance, data=request.data)
        if self.authorization():
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)

    def destroy(self, request, *args, **kwargs):
        comment_id = self.request.resolver_match.kwargs['comment_id']
        instance = get_object_or_404(Comment, id=comment_id)

        if self.authorization(request, instance):
            instance.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
