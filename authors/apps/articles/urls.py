from django.urls import path

from .views import (
    CreateArticleAPIView, RateArticleAPIView, CommentArticleAPIView,
    LikeArticleAPIView, FavouriteArticleAPIView, ListAuthArticlesAPIView,
    ListArticlesAPIView, ArticlesSearchFeed, ListArticleAPIView
)

urlpatterns = [
    path('articles/', CreateArticleAPIView.as_view()),
    path('articles/<int:article_id>', CreateArticleAPIView.as_view()),
    path('articles/me/', ListAuthArticlesAPIView.as_view()),
    path('articles/all/', ListArticlesAPIView.as_view()),
    path('articles/single/<int:article_id>', ListArticleAPIView.as_view()),
    path('articles/<int:article_id>/comment/', CommentArticleAPIView.as_view()),
    path('articles/<int:article_id>/rating/', RateArticleAPIView.as_view()),
    path('articles/<int:article_id>/favourite/',
         FavouriteArticleAPIView.as_view()),
    path('articles/<int:article_id>/likes/', LikeArticleAPIView.as_view()),
    path('articles/<int:article_id>/', LikeArticleAPIView.as_view()),
    path('articles/<int:article_id>/favourite/',
         FavouriteArticleAPIView.as_view()),

    path('articles/search', ArticlesSearchFeed.as_view())
]
