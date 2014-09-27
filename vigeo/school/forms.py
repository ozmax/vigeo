from django.contrib.auth.models import User, Group
from django.forms import ModelForm, Form, widgets, RadioSelect
from django import forms
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
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']
        fname = self.cleaned_data['first_name']
        lname = self.cleaned_data['last_name']
        email = self.cleaned_data['email']
        user = User.objects.create_user(username=username,
            password=password,
            email=email)
        user.first_name = fname
        user.last_name = lname
        user.save()
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


class QuizForm(Form):
    
    def __init__(self, *args, **kwargs):
        super(QuizForm, self).__init__(*args, **kwargs)
        object_list = Question.objects.all().order_by('?')[:10]
        for q in object_list:
            CHOICES = (
                (q.correct_answer, q.correct_answer),
                (q.possible_answer0, q.possible_answer0),
                (q.possible_answer1, q.possible_answer1)
                )
            self.fields[q.title] =\
                forms.ChoiceField(choices=CHOICES,widget=widgets.RadioSelect())
        
    
