from rest_framework import generics, viewsets
from rest_framework.permissions import AllowAny
from .serializers import PostSerializer
from .models import Post


class PostView(generics.ListAPIView):
    queryset = Post.objects.all().order_by("-created_at")
    serializer_class = PostSerializer
    permission_classes = (AllowAny,)


class PostDetailView(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (AllowAny,)


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (AllowAny,)

    def perform_create(self, serializer, **kwargs):
        if self.request.user.is_anonymous:
            serializer.save(created_by=None)
        else:
            serializer.save(created_by=self.request.user)
