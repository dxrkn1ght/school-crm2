from django.urls import path
from . import views


app_name = 'subjects'

urlpatterns = [
    path('list/', views.subjects_list, name='list'),
    path('add/', views.subject_add, name='subject-add'),
    path('detail/<int:subject_id>/', views.subject_detail, name='detail'),
    path('update/<int:subject_id>/', views.subject_update, name='update'),
    path('delete/<int:subject_id>/', views.subject_delete, name='delete'),
]