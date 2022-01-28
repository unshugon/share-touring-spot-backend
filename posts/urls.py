from django.urls import path, include

urlpatterns = [
    path("spots/", include("posts.spots.urls"), name="spots"),
]
