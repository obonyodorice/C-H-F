from django.urls import path
from . import views

app_name = 'funds' 

urlpatterns = [
    path('', views.fund_list, name='fund_list'),
    path('create/', views.fund_create, name='fund_create'),
    path('<int:pk>/', views.fund_detail, name='fund_detail'),
    path('<int:pk>/update/', views.fund_update, name='fund_update'),
    path('<int:pk>/delete/', views.fund_delete, name='fund_delete'),
]