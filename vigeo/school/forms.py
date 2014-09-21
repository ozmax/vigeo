from django.contrib.auth.models import User
from django.forms import ModelForm, widgets
from django.contrib.auth.models import Group

from school.models import Student, Lesson, Category, Question


class StudentForm(ModelForm):

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'password', 'email']
        widgets = {'password': widgets.PasswordInput()}


    def __init__(self, *args, **kwargs):
        super(StudentForm, self).__init__(*args, **kwargs)
        self.fields['username'].help_text = None

    def save(self):
        user = super(StudentForm, self).save()
        g = Group.objects.get(name='student') 
        g.user_set.add(user)
        Student.objects.create(user_id=user.id)


class LessonForm(ModelForm):
    
    class Meta:
        model = Lesson


class CategoryForm(ModelForm):
    
    class Meta:
        model = Category


class QuestionForm(ModelForm):
    
    class Meta:
        model = Question
