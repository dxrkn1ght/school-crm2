from django.urls import path
from . import views


app_name = 'teachers'

urlpatterns = [
    path('list/', views.teachers_list, name='list'),
    path('add/', views.teacher_add, name='teacher-add'),
    path('detail/<int:teacher_id>/', views.teacher_detail, name='detail'),
    path('update/<int:teacher_id>/', views.teacher_update, name='update'),
    path('delete/<int:teacher_id>/', views.teacher_delete, name='delete'),
]