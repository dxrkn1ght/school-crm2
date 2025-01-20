from django.db import models


class Group(models.Model):
    name = models.CharField(max_length=100)
    teacher = models.OneToOneField('teachers.Teacher', on_delete=models.CASCADE, related_name='group')

    def __str__(self):
        return self.name