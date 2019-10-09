from django.db.models import Q

from rest_framework.generics import (
CreateAPIView,
ListAPIView,
RetrieveAPIView,
RetrieveUpdateAPIView,
DestroyAPIView
)
from posts.models import Post
from .serializers import PostSerializer,PostCreateSerializer

from .pagination import Pagenumberpagination, Limitoffsetpagination

class PostCreateApiView(CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostCreateSerializer

    def perform_create(self,serializer):
        serializer.save(user=self.request.user)

class PostListApi(ListAPIView):
    serializer_class = PostSerializer
    pagination_class = Limitoffsetpagination #Pagenumberpagination

    def get_queryset(self,*args,**kwargs):
        queryset_list = Post.objects.all()
        query = self.request.GET.get("q")
        if query:
            queryset_list = queryset_list.filter(
                Q(title__icontains=query)|
                Q(content__icontains=query)|
                Q(user__first_name__icontains=query)|
                Q(user__last_name__icontains=query)
            ).distinct()

        return queryset_list




class PostDetailAPIView(RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    lookup_field = 'slug'

class PostUpdateApiView(RetrieveUpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    lookup_field = 'slug'

    def perform_update(self,serializer):
        serializer.save(user=self.request.user)

class PostDeleteApiView(DestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    lookup_field = 'slug'

