from django.urls import path
from . import views

urlpatterns = [
    path("posts/", views.PostView.as_view(), name="post"),
    path("post/<int:pk>", views.PostDetailView.as_view(), name="post_detail")
]
