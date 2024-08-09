from django.urls import path
from django.contrib.auth import views as auth_views
from cmsapp import views

urlpatterns = [
    path('', views.index, name='index'),
    path('category/<int:category_id>/', views.category_detail, name='category_detail'),
    path('items/', views.item_list, name='item_list'),
    path('item/<int:item_id>/', views.item_detail, name='item_detail'),
    path('item/new/', views.item_create, name='item-create'),
    path('item/<int:pk>/edit/', views.item_update, name='item-update'),
    path('item/<int:pk>/delete/', views.item_delete, name='item-delete'),
    path('search/', views.search, name='search'),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]