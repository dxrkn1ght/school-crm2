from django.db import models


class Student(models.Model):
    full_name = models.CharField(max_length=150)
    date_of_birth = models.DateField()
    phone_number = models.CharField(max_length=15)
    address = models.TextField()
    photo = models.ImageField(upload_to='students-images/')
    group = models.ForeignKey('groups.Group', on_delete=models.CASCADE, related_name='students')

    def __str__(self):
        return self.full_name
