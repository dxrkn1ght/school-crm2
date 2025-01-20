from django.shortcuts import render, redirect, get_object_or_404
from .models import Student
from groups.models import Group


def students_list(request):
    students = Student.objects.all()
    students_count = students.count()
    ctx = {'students':students, 'students_count':students_count}
    return render(request, 'students/students-list.html', ctx)

def student_add(request):
    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        date_of_birth = request.POST.get('date_of_birth')
        phone_number = request.POST.get('phone_number')
        address = request.POST.get('address')
        photo = request.FILES.get('photo')
        group_id = request.POST.get('group')
        if full_name and date_of_birth and phone_number and address and photo and group_id:
            group = Group.objects.get(id=group_id)
            student = Student.objects.create(
            full_name = full_name,
            date_of_birth = date_of_birth,
            phone_number = phone_number,
            address = address,
            photo = photo,
            group = group,
            )
            student.save()
            return redirect('students:list')
    groups = Group.objects.all()
    ctx = {'groups': groups}
    return render(request, 'students/student-add.html', ctx)

def student_detail(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    ctx = {'student':student}
    return render(request, 'students/student-detail.html', ctx)

def student_update(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        date_of_birth = request.POST.get('date_of_birth')
        phone_number = request.POST.get('phone_number')
        address = request.POST.get('address')
        photo = request.FILES.get('photo')
        group_id = request.POST.get('group')
        if full_name and date_of_birth and phone_number and address and group_id:
            student.full_name = full_name
            student.date_of_birth = date_of_birth
            student.phone_number = phone_number
            student.address = address
            if photo:
                student.photo = photo
            group = Group.objects.get(id=group_id)
            student.group = group
            student.save()
            return redirect('students:detail', student.id)
    groups = Group.objects.all()
    ctx = {
        'student':student,
        'groups':groups
    }
    return render(request, 'students/student-add.html', ctx)

def student_delete(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    student.delete()
    return redirect('students:list')