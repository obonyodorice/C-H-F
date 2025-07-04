from django.urls import path
from . import views

app_name = 'pledges' 

urlpatterns = [
    path('', views.pledge_list, name='pledge_list'),
    path('create/', views.pledge_create, name='pledge_create'),
    path('<int:pk>/', views.pledge_detail, name='pledge_detail'),
    path('<int:pk>/update/', views.pledge_update, name='pledge_update'),
    path('<int:pk>/delete/', views.pledge_delete, name='pledge_delete'),
]