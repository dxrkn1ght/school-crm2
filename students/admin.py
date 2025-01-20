from django.contrib import admin

from .models import Student


class StudentInline(admin.StackedInline):
    model = Student
    extra = 0

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'date_of_birth', 'phone_number', 'address', 'group')
    list_filter = ('full_name', 'group')
    search_fields = ('full_name',)