from django.urls import path
from .views import MovieListView, MovieDetailView, login_register, logout_view

urlpatterns = [
    path('', login_register, name='login_register'),
    path('movies/', MovieListView.as_view(), name='movie_list'),
    path('movies/<int:pk>/', MovieDetailView.as_view(), name='movie_detail'),
    path('logout/', logout_view, name='logout'),
]
