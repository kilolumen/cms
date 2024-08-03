from django.urls import path
from cmsapp import views

urlpatterns = [
    path('', views.index, name='index'),
    path('category/<int:category_id>/', views.category_detail, name='category_detail'),
    path('item/<int:item_id>/', views.item_detail, name='item_detail'),
    path('search/', views.search, name='search'),
]