from django.urls import path
from .views import BlogPostListView, BlogPostDetailView, BlogPostCreateView, BlogPostUpdateView, BlogPostDeleteView

urlpatterns = [
    path('', BlogPostListView.as_view(), name='blogpost_list'),
    path('<int:pk>/', BlogPostDetailView.as_view(), name='blogpost_detail'),
    path('new/', BlogPostCreateView.as_view(), name='blogpost_new'),
    path('<int:pk>/edit/', BlogPostUpdateView.as_view(), name='blogpost_edit'),
    path('<int:pk>/delete/', BlogPostDeleteView.as_view(), name='blogpost_delete'),
]
