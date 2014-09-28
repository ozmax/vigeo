from django.contrib.auth.models import User, Group
from django import forms
from school.models import Student, Lesson, Category, Question


class StudentForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'password', 'email']
        widgets = {'password': forms.widgets.PasswordInput()}


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


class LessonForm(forms.ModelForm):
    
    class Meta:
        model = Lesson


class CategoryForm(forms.ModelForm):
    
    class Meta:
        model = Category


class QuestionForm(forms.ModelForm):
    
    class Meta:
        model = Question


class QuizForm(forms.Form):
    
    def __init__(self, *args, **kwargs):
        self.question_nr = 3
        keys = kwargs.pop('keys', None)
        arakse = kwargs.pop('f_nr', None)
        super(QuizForm, self).__init__(*args, **kwargs)
        if not keys:
            object_list = Question.objects.all().order_by('?')[:self.question_nr]
            for q in object_list:
                CHOICES = (
                    (q.correct_answer, q.correct_answer),
                    (q.possible_answer0, q.possible_answer0),
                    (q.possible_answer1, q.possible_answer1)
                    )
                self.fields[q.title] =\
                    forms.ChoiceField(choices=CHOICES,widget=forms.widgets.RadioSelect())
        else:
            print keys
            self.current_nr = len(keys)

            for key in keys:
                q = Question.objects.get(title=key)
                CHOICES = (
                    (q.correct_answer, q.correct_answer),
                    (q.possible_answer0, q.possible_answer0),
                    (q.possible_answer1, q.possible_answer1)
                    )
                self.fields[q.title] =\
                    forms.ChoiceField(choices=CHOICES,widget=forms.widgets.RadioSelect())
        
    def clean(self):
        print self.current_nr
        print 'was here'
        if self.current_nr != self.question_nr:
            msg = 'foobar'
            raise forms.ValidationError(msg)
        return f_nr
