from django.urls.conf import include
from rest_framework import routers
from django.urls import path
from posts.spots import views


router = routers.DefaultRouter()

urlpatterns = [
    path("list/", views.PostView.as_view(), name="list"),
    path("<int:pk>/", views.PostDetailView.as_view(), name="detail"),
    path("new", views.PostViewSet.as_view(), name="new"),
    path("", include(router.urls)),
]
