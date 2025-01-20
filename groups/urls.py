from django.urls import path
from . import views


app_name = 'groups'

urlpatterns = [
    path('list/', views.groups_list, name='list'),
    path('add/', views.group_add, name='group-add'),
    path('detail/<int:group_id>/', views.group_detail, name='detail'),
    path('update/<int:group_id>/', views.group_update, name='update'),
    path('delete/<int:group_id>/', views.group_delete, name='delete'),
]