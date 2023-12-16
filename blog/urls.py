from django.urls import path
from .views import BlogListView, BlogCreateView, BlogDetailView, PostDeleteView, PostUpdateView

app_name='blog'

urlpatterns = [
    path("", BlogListView.as_view(), name="home"),
    path("create/", BlogCreateView.as_view(), name="create"),
    path("<int:pk>/", BlogDetailView.as_view(), name="detail"),
    path("<int:pk>/update/", PostUpdateView.as_view(), name="update"),
    path("<int:pk>/delete/", PostDeleteView.as_view(), name="delete"),

]
