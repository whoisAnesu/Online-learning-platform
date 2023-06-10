from django.contrib import admin
from .models import Question, Answer, Quiz, Result, Results, UserCoursework, Mycoursework 


class AnswerInline(admin.TabularInline):
    model = Answer
    
    
class QuestionAmin(admin.ModelAdmin):
    inlines = [AnswerInline]
    
admin.site.register(Question, QuestionAmin)
admin.site.register(Answer)
admin.site.register(Quiz)
admin.site.register(Result)
admin.site.register(Results)
admin.site.register(UserCoursework)
admin.site.register(Mycoursework)
