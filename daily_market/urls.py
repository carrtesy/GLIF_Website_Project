from django.urls import include, path
from django.contrib import admin
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView

urlpatterns = [
    path('', PostListView.as_view(), name='daily_market-index'),
    path('<int:pk>', PostDetailView.as_view(), name = "daily_market-detail"),
    path('new', PostCreateView.as_view(), name = "daily_market-new"),
    path('<int:pk>/update', PostUpdateView.as_view(), name = "daily_market-update"),
    path('<int:pk>/delete', PostDeleteView.as_view(), name = "daily_market-delete"),
]