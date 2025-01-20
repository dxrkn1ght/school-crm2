from django.shortcuts import render, redirect, get_object_or_404
from .models import Group
from teachers.models import Teacher
from students.models import Student


def home(request):
    return render(request, 'index.html')

def groups_list(request):
    groups = Group.objects.all()
    group_count = groups.count()
    ctx = {'groups': groups, 'group_count':group_count}
    return render(request, 'groups/groups-list.html', ctx)

def group_add(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        teacher_id = request.POST.get('teacher')
        student_ids = request.POST.getlist('students')
        if name and teacher_id and student_ids:
            teacher = Teacher.objects.get(id=teacher_id)
            students = Student.objects.filter(id__in=student_ids)
            group = Group.objects.create(
                name=name,
                teacher=teacher
            )
            group.students.set(students)
            group.save()
            return redirect('groups:list')
    teachers = Teacher.objects.all()
    students = Student.objects.all()
    ctx = {'teachers': teachers, 'students': students}
    return render(request, 'groups/group-add.html', ctx)

def group_detail(request, group_id):
    group = get_object_or_404(Group, pk=group_id)
    students = group.students.all()
    ctx = {'group':group, 'students':students}
    return render(request, 'groups/group-detail.html', ctx)

def group_update(request, group_id):
    group = get_object_or_404(Group, pk=group_id)
    if request.method == 'POST':
        name = request.POST.get('name')
        teacher_id = request.POST.get('teacher')
        student_ids = request.POST.getlist('students')
        if name and teacher_id and student_ids:
            group.name = name
            group.teacher = Teacher.objects.get(id=teacher_id)
            students = Student.objects.filter(id__in=student_ids)
            group.students.set(students)
            group.save()
            return redirect('groups:detail', group.id)
    teachers = Teacher.objects.all()
    students = Student.objects.all()
    ctx = {
        'group':group,
        'teachers':teachers,
        'students':students,
    }
    return render(request, 'groups/group-add.html', ctx)

def group_delete(request, group_id):
    group = get_object_or_404(Group, pk=group_id)
    group.delete()
    return redirect('groups:list')