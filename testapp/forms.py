from django import forms
from testapp.models import *

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
        widgets = {
            'photo': forms.FileInput(),
            'video': forms.FileInput(),
        }

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'
        widgets = {
            'year': forms.DateInput(attrs={'type': 'date'}),

        }

class LibraryForm(forms.ModelForm):
    class Meta:
        model = Library
        fields = '__all__'
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
        }
