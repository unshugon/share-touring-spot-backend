from rest_framework import generics
from rest_framework.permissions import AllowAny
from .serializers import PostSerializer
from .models import Post
from django.contrib.gis.geos.point import Point
from rest_framework.response import Response
from rest_framework import status


class PostView(generics.ListAPIView):
    queryset = Post.objects.all().order_by("-created_at")
    serializer_class = PostSerializer
    permission_classes = (AllowAny,)


class PostDetailView(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (AllowAny,)


class PostViewSet(generics.CreateAPIView):
    serializer_class = PostSerializer
    permission_classes = (AllowAny,)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(
            serializer,
            lat=float(request.POST["latitude"]),
            lng=float(request.POST["longitude"]),
        )
        headers = self.get_success_headers(serializer.data)
        return Response(
            serializer.data, status=status.HTTP_201_CREATED, headers=headers
        )

    def perform_create(self, serializer, lat, lng, **kwargs):
        location = Point((lat, lng))
        if self.request.user.is_anonymous:
            serializer.save(created_by=None, location=location)
        else:
            serializer.save(created_by=self.request.user, location=location)
