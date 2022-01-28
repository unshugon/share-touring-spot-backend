from django.urls.conf import include
from rest_framework import routers
from django.urls import path
from posts.spots import views


router = routers.DefaultRouter()
router.register("new", views.PostViewSet)

urlpatterns = [
    path("list/", views.PostView.as_view(), name="list"),
    path("list/<str:pk>/", views.PostDetailView.as_view(), name="detail"),
    path("", include(router.urls)),
]
