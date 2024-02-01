from django.urls import path
from . import views


app_name = 'home'
urlpatterns = [
    path('home_header/', views.HomeHeaderView.as_view(), name='home_header'),
    path('home_footer/', views.HomeFooterView.as_view(), name='home_footer'),
    path('home_content/', views.HomeContentView.as_view(), name='home_content'),
    path('team_content/', views.TeamContentView.as_view(), name='team_content'),
    path('more_landing/', views.MoreLandingView.as_view(), name='more_landing'),
    path('paper_pdf/', views.PaperPdfView.as_view(), name='paper_pdf'),
    path('connected/', views.ConnectedView.as_view(), name='connected'),
    path('search_title/', views.SearchPdfTitleView.as_view({'get': 'list'}), name='search_title'),
    path('search_category/', views.SearchPdfCategoryView.as_view({'get': 'list'}), name='search_category'),
    path('search_date/', views.SearchPdfDateView.as_view({'get': 'list'}), name='search_date'),

]
