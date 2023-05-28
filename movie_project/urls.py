from django.urls import path
from movie_test import views


urlpatterns = [
    path('', views.home, name='home'),
    path('films/', views.films, name='films'),
    path('series/', views.series, name='series'),
    path('contact/', views.contact, name='contact'),
    path('media_detail/<int:Media_id>/', views.film_detail, name='film_detail'),
    # path('add_rating/<int:Media_id>/', views.add_rating, name='add_rating'),
    path('media/genre/<str:movie_genre>/', views.film_genre, name='media_genre'),
    path('search/', views.search, name='search'),
    path('media/year/<str:movie_year>/', views.film_year, name='media_year'),
]
