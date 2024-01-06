from django.urls import path
from . import views


app_name = 'home'
urlpatterns = [
    path('home_header/', views.HomeHeaderView.as_view(), name='home_header'),
    path('home_footer/', views.HomeFooterView.as_view(), name='home_footer'),
    path('home_content/', views.HomeContentView.as_view(), name='home_content'),
]
