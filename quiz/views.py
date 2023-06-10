from django.http import JsonResponse
from django.shortcuts import render, HttpResponse, redirect
from .models import Quiz, Question, Answer, Result, Results, Mycoursework
from django.contrib.auth.decorators import login_required
from .forms import QuizForm
from django.views.generic import ListView
from django.http import JsonResponse 


class QuizListView(ListView):
    model = Quiz 
    template_name = 'quiz/quiz_home.html'
    
def quiz_view(request, pk):
    quiz = Quiz.objects.get(pk=pk)
    return render(request, 'quiz/quiz.html', {'obj': quiz})



@login_required(login_url='/login')
def createQuiz(request):
    form = QuizForm()
    if request.method == 'POST':
        form = QuizForm(request.POST)
        if form.is_valid():
            quiz = form.save(commit=False)
            quiz.save()
            return redirect('main-view')
    
    context = {'form': form}
    return render(request, 'base/quiz_form.html', context)


def quiz_data_view(request, pk):
    quiz = Quiz.objects.get(pk=pk)
    questions = []
    for q in quiz.get_questions():
        answers = []
        for a in q.get_answers():
            answers.append(a.text)
        questions.append({str(q):answers})
    return JsonResponse({
        'data':questions,
        'time':quiz.time,
    })
    
def save_quiz_view(request, pk):
    # print(request.POST)
    if request.accepts(pk):
        questions = []
        data = request.POST 
        data_ = dict(data.lists())
        
        data_.pop('csrfmiddlewaretoken')
        
        for k in data_.keys():
            print('key: ', k)
            question = Question.objects.get(text=k)
            questions.append(question)
        print(questions)
        
        user = request.user
        quiz = Quiz.objects.get(pk=pk)
        
        score = 0
        multiplier = 100 / quiz.number_of_questions
        results = []
        correct_answer = None
        
        for q in questions:
            a_selected = request.POST.get(q.text)
            
            if a_selected != "":
                question_answers = Answer.objects.filter(question=q)
                for a in question_answers:
                    if a_selected == a.text:
                        if a.correct:
                            score += 1
                            correct_answer = a.text
                    else:
                        if a.correct:
                            correct_answer = a.text
                results.append({str(q):{'correct_answer': correct_answer, 'answered': a_selected}})
            else:
                results.append({str(q): 'not answered'})
            
        
        score_ = score * multiplier
        Result.objects.create(quiz=quiz, user=user, score=score_)
        Mycoursework.objects.create(user=request.user, course_quiz=quiz, the_mark=score_, the_course=quiz.course)
        
        if score_ >= quiz.required_score_to_pass:
            return JsonResponse({'passed': True, 'score':score_, 'results': results})
        else:    
            return JsonResponse({'passed': False,'score':score_, 'results': results})
        
        

