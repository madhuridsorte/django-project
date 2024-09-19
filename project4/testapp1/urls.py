from django.urls import path
from testapp1 import views

urlpatterns = [
    path('', views.main_view),
    path('movie/', views.movie_view),
    path('sports/', views.sports_view),
    path('politics/', views.politics_view),
]
