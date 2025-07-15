from django.urls import path
from . import views
app_name = 'contributions'

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create_contribution, name='create_contribution'),
    path('update/<int:id>/', views.update_contribution, name='update_contribution'),
    path('<int:pk>/', views.contribution_detail, name='contribution_detail'),
    path('delete/<int:id>/', views.delete_contribution, name='delete_contribution'),
    path('list/', views.list_contributions, name='list_contributions'),
]