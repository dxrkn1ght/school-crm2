from django.contrib import admin

from .models import Group
from students.admin import StudentInline


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ('name', 'teacher', 'students_count')
    list_filter = ('name', 'teacher')
    search_fields = ('name', 'teacher__first_name', 'teacher__last_name')
    inlines = [StudentInline]

    def students_count(self, obj):
        return obj.students.count()
    students_count.short_description = 'Number of Students'