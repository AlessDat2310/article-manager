from django.urls import path
from .views import ArticleListView, ArticleDetailView, ArticleCreateView, ArticleUpdateView, ArticleDeleteView
from . import views

urlpatterns = [
    path('', views.ArticleListView.as_view(), name='article-list'),
    path('/all', views.ArticleListView.as_view(), name="all_articles"),
    path('<int:pk>/', views.ArticleDetailView.as_view(), name='article-detail'),
    path('<int:pk>/edit/', ArticleUpdateView.as_view(), name='article-edit'),
    path('<int:pk>/delete/', ArticleDeleteView.as_view(), name='article-delete'),
    path('new/', ArticleCreateView.as_view(), name='article-create'),
         
]