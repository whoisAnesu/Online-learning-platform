from django.shortcuts import render, redirect 
from django.http import HttpResponse
from django.contrib import messages 
from django.contrib.auth.decorators import login_required  
from django.contrib.auth import authenticate, login, logout  
from django.contrib.auth.models import User 
from mychatapp.models import Profile
from quiz.models import UserCoursework, Mycoursework
from .models import Category, News, Comments
from .forms import CommentsForm
from quiz.forms import QuizForm, QuestionForm, AnswerForm, AnswerFormSet
from quiz.models import Question, Answer, Quiz
from django.db.models import Q
from django.forms import inlineformset_factory


def home(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    news = News.objects.filter(Q(title__icontains= q) | 
                                Q(journalist__icontains=q) |
                                Q(summary__icontains=q))
    news_comments = Comments.objects.all()
    context = {"news": news, "news_comments": news_comments}
    return render(request, "UsersAuth/home_page.html", context)

def loginPage(request):
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'User does not exist')
            
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Username Or Password does not exist')
    context = {}
    return render(request, 'UsersAuth/login_page.html', context)


def logoutUser(request):
    logout(request)
    return redirect('login')

def signup(request):
    
    if request.method == "POST":
        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        student = User.objects.create_user(username, email, password)
        student.first_name = first_name
        student.last_name = last_name 
        
        student.save()
        
        messages.success(request, "The Student has been successfully created")
        
        return redirect('home')
        
    
    return render(request, 'UsersAuth/register.html')


def student_profile(request, pk):
    profile = Profile.objects.get(id=pk)
    context = {'profile': profile}
    return render(request, 'UsersAuth/student_profile.html', context)


def news_page(request, pk):
    article = News.objects.get(id=pk)
    newscomment = article.comments_set.all()
    if request.method == "POST":
        comment = Comments.objects.create(
            creator=request.user, 
            article=article,
            text = request.POST.get('body')
        )
        return redirect('news_page',pk=article.id)
    context = {'article': article, 'newscomment': newscomment}
    return render(request, 'UsersAuth/news_page.html', context)

def deleteComment(request, pk):
    del_comment = Comments.objects.get(id=pk)
    
    if request.method == "POST":
        del_comment.delete()
        return redirect('home')
    return render(request , 'base/delete.html', {'obj': del_comment})


def deleteComment2(request, pk):
    del_comment = Comments.objects.get(id=pk)
    
    if request.method == "POST":
        del_comment.delete()
        return redirect('news_page', pk=del_comment.article.id)
    return render(request , 'base/delete.html', {'obj': del_comment})

def save_user_marks(request, pk):
    myuser = UserCoursework.objects.get(user_id=pk)
    mymark = myuser.mycoursework.all()
    context = {'mymark': mymark}
    return render(request, 'UsersAuth/coursework.html', context)

def createQuiz(request):
    form = QuizForm()
    if request.method == 'POST':
        form = QuizForm(request.POST)
        if form.is_valid():
            quiz = form.save(commit=False)
            quiz.save()
            return redirect('home')
    
    context = {'form': form}
    return render(request, 'UsersAuth/quiz_form.html', context)

def createQuestion(request):
    allquiz = Quiz.objects.all()
    if request.method == "POST":
        question = request.POST.get('question')
        quis = request.POST.get('quis')
        answer = request.POST.get('answer')
        correct = request.POST.get('correct')
        
        TheQuestion = Question.objects.create(text=question, quiz=quis)
        TheAnswer = Answer.objects.create(text=answer, correct=correct, question=question)
        TheQuestion.save()
        TheAnswer.save()
    
    context = {'allquiz': allquiz, }
    return render(request, 'UsersAuth/quiz_form.html', context)