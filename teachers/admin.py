from django.contrib import admin
from django.contrib.admin import StackedInline

from .models import Teacher


class TeacherInline(StackedInline):
    model = Teacher
    extra = 0

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'subject', 'phone_number', 'email', 'years_of_work')
    list_filter = ('first_name', 'last_name', 'subject')
    search_fields = ('first_name', 'last_name', 'subject')