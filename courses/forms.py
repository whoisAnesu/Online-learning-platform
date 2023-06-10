from django import forms 

from .models import Book, Video, Submit, Assignment, RegProfile

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('title', 'author', 'pdf')
        
        
class VideoForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = ('caption','video')
        

class SubmitForm(forms.ModelForm):
    class Meta:
        model = Submit
        fields = ('assignment', 'pdf_sub', 'course',)
        exclude = ['owner', ]
        
class AssignmentForm(forms.ModelForm):
    class Meta:
        model = Assignment
        fields = ('title', 'author', 'pdf_ass', 'course')
        exclude = ['done', ]

class RegisterForm(forms.ModelForm):
    class Meta:
        model = RegProfile
        fields = ('courses', 'registerd',)
        exclude = ['user', 'name',]