from django.db import models
import random
from django.contrib.auth.models import User
from courses.models import Course

DIFF_CHOICES = (
    ('easy', 'easy'),
    ('medium', 'medium'),
    ('hard', 'hard'),
)

class Quiz(models.Model):
    name = models.CharField(max_length=120)
    topic = models.CharField(max_length=120)
    number_of_questions = models.IntegerField()
    time = models.IntegerField(help_text="duration of the quiz in minutes")
    required_score_to_pass = models.IntegerField(help_text="required score in %")
    difficulty = models.CharField(max_length=6, choices=DIFF_CHOICES)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, null=True, blank=True)
    
    def __str__(self):
        return f"{self.name}-{self.topic}"
    
    def get_questions(self):
        questions = list(self.question_set.all())
        random.shuffle(questions)
        return questions[:self.number_of_questions]
    
    class Meta:
        verbose_name_plural = 'Quizes'
        
class Question(models.Model):
    text = models.CharField(max_length=200)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return str(self.text)

    def get_answers(self):
        return self.answer_set.all() 

    
class Answer(models.Model):
    text = models.CharField(max_length=200)
    correct = models.BooleanField(default=False)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"question: {self.question.text}, answer: {self.text}, correct: {self.correct}"
        
class Result(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    score= models.FloatField()
    
    def __str__(self):
        return str(self.pk)
    
class Results(models.Model):
    results_user = models.ForeignKey(User, on_delete=models.CASCADE)
    results_course = models.CharField(max_length=200)
    results_mark = models.IntegerField(help_text= "%")
    results_remark = models.CharField(max_length=200)
    results_classification = models.CharField(max_length=5)

class Mycoursework(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course_quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    the_course = models.CharField(max_length=200, blank=True, null=True)
    the_mark = models.IntegerField(help_text= "%")
    the_remark = models.CharField(max_length=200, blank=True, null=True)
    the_classification = models.CharField(max_length=5, blank=True, null=True)
    
    def __str__(self):
        return str(self.user)

class UserCoursework(models.Model):
    mycoursework = models.ManyToManyField(Mycoursework)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    
    def __str__(self):
        return str(self.user)
    
