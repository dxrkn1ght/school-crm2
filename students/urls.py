from django.urls import path
from . import views


app_name = 'students'

urlpatterns = [
    path('list/', views.students_list, name='list'),
    path('add/', views.student_add, name='student-add'),
    path('detail/<int:student_id>/', views.student_detail, name='detail'),
    path('update/<int:student_id>/', views.student_update, name='update'),
    path('delete/<int:student_id>/', views.student_delete, name='delete'),
]