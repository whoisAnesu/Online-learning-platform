from django.shortcuts import render, redirect
from .models import Course, Assignment, Submit, RegProfile
from .forms import AssignmentForm, SubmitForm, BookForm, RegisterForm
from django.core.files.storage import FileSystemStorage


def course(request, pk):
    course = Course.objects.get(id=pk)
    books = course.books.all()
    video = course.tutorial.all()
    students = course.students.all()
    assignments = course.assignment_set.all()
    submition = course.submit_set.all()
    context = {
        'course': course, 
        'books': books, 
        'video': video, 
        'students': students,
        'assignments': assignments,
        'submition': submition,
        }
    return render(request, 'courses/course_home.html', context)

def coursesAll(request):
    all_courses = Course.objects.all()
    context = {'all_courses': all_courses}
    return render(request, 'courses/courses_all.html', context)

def upload(request):
    context = {}
    if request.method == 'POST':
        uploaded_file = request.FILES['document']
        fs = FileSystemStorage()
        name = fs.save(uploaded_file.name, uploaded_file)
        url = fs.url(name)
        context['url'] = fs.url(name)
    return render(request, 'courses/upload.html', context)

def uploadAss(request):
    if request.method == "POST":
        form = AssignmentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = AssignmentForm()
        
    context = {'form': form}    
    return render(request, 'courses/myform.html', context)

def submitAss(request):
    if request.method == "POST":
        form = SubmitForm(request.POST, request.FILES)
        if form.is_valid():
            assign = form.save(commit=False)
            assign.owner = request.user
            assign.save()
            return redirect('home')
    else:
        form = SubmitForm()
        
    context = {'form': form}    
    return render(request, 'courses/myform.html', context)

def upload_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = BookForm()
        
    context =  {
        'form': form
    }
    return render(request, "myform.html",context)

def video(request, pk):
    course = Course.objects.get(id=pk)
    video = course.tutorial.all()
    context = {'course': course, 'video': video}
    return render(request, 'courses/videos.html', context)

def books(request, pk):
    course = Course.objects.get(id=pk)
    books = course.books.all()
    context = {'course': course, 'books': books}
    return render(request, 'courses/books.html', context)

def myCourses(request, pk):
    students = RegProfile.objects.get(user_id=pk)
    courses = students.courses.all()
    context = {'students': students, 'courses': courses}
    return render(request, 'courses/mycourses.html', context)

def registerCourses(request, pk):
    student = RegProfile.objects.get(user_id=pk)
    if request.method == "POST":
        form = RegisterForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('mycourses', pk=pk)
    else:
        form = RegisterForm()
    context = {'form': form}    
    return render(request, 'courses/myform.html', context)