from django.urls import path

from . import views

app_name = 'movies'
urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.loginUser, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('register/', views.register, name='register'),
    path('<int:movie_id>/', views.detail, name='detail'),
    path('location/', views.location, name='location'),
    path('search/', views.search, name='search'),
    path('recommend/', views.recommend, name='recommend'),
]
