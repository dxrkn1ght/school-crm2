from django.contrib import admin

from teachers.admin import TeacherInline
from .models import Subject


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'teachers_count')
    list_filter = ('name',)
    search_fields = ('name',)
    inline = [TeacherInline]

    def teachers_count(self, obj):
        return obj.teachers.count()
    teachers_count.short_description = 'Number of Teachers'