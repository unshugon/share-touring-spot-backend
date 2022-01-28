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

    def perform_create(self, serializer, **kwargs):
        if self.request.user:
            serializer.save(created_by=self.request.user)
        else:
            serializer.save(created_by=None)
