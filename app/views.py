from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,redirect
from .models import Student,Course
from django.views.generic import ListView, DetailView

def home(request):
    return render(request,'home.html')

def studentlist(request):
    students = Student.objects.all()
    return render(request,'studentlist.html',{'students':students})

def courselist(request):
    courses = Course.objects.all()
    return render(request,'courselist.html',{'courses':courses})


def register(request):
    if request.method == "POST":
        usn = request.POST['usn']
        name = request.POST['name']
        sem = request.POST['sem']
        subcode = request.POST['subcode']
        subname = request.POST['subname']
        credits = request.POST['credits']

        # Create or get the course
        course= Course.objects.create(
            subcode=subcode,
            subname=subname,
            credits=credits
        )
        

        # Create the student
        student = Student.objects.create(
            usn=usn,
            name=name,
            sem=sem
        )

        # Link student to course
        student.courses.add(course)

        return redirect('/studentlist/')

    return render(request, 'register.html')

# def enrolledlist(request):
#     students=Student.objects.all()
#     return render(request,'enrolledlist.html',{'students':students})

from django.shortcuts import render
from .models import Student, Course

def enrolledlist(request):
    selected_course = request.GET.get('course')
    students = Student.objects.filter(courses__subcode=selected_course)
    return render(request, 'enrolledlist.html', {
        'courses': Course.objects.all(),
        'selected_course': selected_course,
        'students': students,
    })



class StudentListView(ListView):
    model = Student
    template_name = 'studentlist.html'
    context_object_name = 'students'


class StudentDetailView(DetailView):
    model = Student
    template_name = 'student_detail.html'
    context_object_name = 'student'