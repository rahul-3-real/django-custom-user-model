from django.urls import path
from . import views

app_name = 'movies'

urlpatterns = [
    path('', views.MovieSelectFormView.as_view(), name="movie-select"),
    path('add/', views.AddMovieFormView.as_view(), name="add-movie"),
]
