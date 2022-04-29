from django.shortcuts import render,redirect
from .models import Student
from .forms import StudentModelForm

def addStudentModelForm(request):
    form = StudentModelForm()
    if request.method == 'POST':
        form =StudentModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_stu')
    template_name = 'StudentApp/addstudent.html'
    context = {'form':form}
    return render(request,template_name,context)

def showStudent(request):
    student = Student.objects.all()
    context = {'student':student}
    template_name = 'StudentApp/showstudent.html'
    return render(request,template_name,context)

def deleteStudent(request,i):
    student = Student.objects.get(stu_id=i)
    print(i)
    if request.method == 'POST':
        student.delete()
        return redirect('show_stu')
    context = {'student':student}
    template_name = 'StudentApp/deletestudent.html'
    return render(request,template_name,context)

def updateStudent(request,i):
    student = Student.objects.get(stu_id=i)
    form = StudentModelForm(instance=student)
    if request.method == 'POST':
        form = StudentModelForm(request.POST,instance=student)
        if form.is_valid():
            form.save()
            return redirect('show_stu')
    context = {'form':form}
    template_name = 'StudentApp/addstudent.html'
    return render(request,template_name,context)
