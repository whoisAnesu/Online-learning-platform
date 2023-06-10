from django.forms import ModelForm, inlineformset_factory 
from .models import Results, UserCoursework, Quiz, Question, Answer

class CourseworkForm(ModelForm):
    class Meta:
        model = UserCoursework 
        fields = '__all__'
        exclude = ['course_user', 'course_quiz', 'the_mark', 'the_classification']
        


class ResultsForm(ModelForm):
    class Meta:
        model = Results 
        fields = '__all__'
        exclude = ['results_user', 'results_course', 'results_mark', 'the_mark'] 
        
        

class QuizForm(ModelForm):
    class Meta:
        model = Quiz 
        fields = '__all__'
        
        
class QuestionForm(ModelForm):
    class Meta:
        model = Question 
        fields = '__all__'
        
class AnswerForm(ModelForm):
    class Meta:
        model = Answer 
        fields = '__all__'
        
AnswerFormSet = inlineformset_factory(
    Question, Answer, form=AnswerForm,
    extra=1, can_delete=False
)