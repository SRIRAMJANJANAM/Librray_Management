from django.shortcuts import render, get_object_or_404, redirect
from testapp.models import *


from .forms import *

def student_view(request):
    students = Student.objects.all()
    return render(request, 'testapp/index.html', {'students': students})

def student_input(request, id=None):
    student = get_object_or_404(Student, id=id) if id else None
    form = StudentForm(request.POST or None, request.FILES or None, instance=student)  # Add request.FILES
    if form.is_valid():
        form.save()
        return redirect('student_view')
    return render(request, 'testapp/add.html', {'form': form})

def student_delete(request, id):
    student = get_object_or_404(Student, id=id)
    student.delete()
    return redirect('student_view')

def book_view(request):
    books = Book.objects.all()
    return render(request, 'testapp/book.html', {'books': books})

def book_input(request, id=None):
    book = get_object_or_404(Book, id=id) if id else None
    form = BookForm(request.POST or None, instance=book)
    if form.is_valid():
        form.save()
        return redirect('book_view')
    return render(request, 'testapp/bookedit.html', {'form': form})

def book_delete(request, id):
    book = get_object_or_404(Book, id=id)
    book.delete()
    return redirect('book_view')


def library_view(request):
    libraries = Library.objects.all()
    return render(request, 'testapp/library.html', {'libraries': libraries})

def library_input(request, id=None):
    library = get_object_or_404(Library, id=id) if id else None
    form = LibraryForm(request.POST or None, instance=library)
    if form.is_valid():
        form.save()
        return redirect('library_view')
    return render(request, 'testapp/libraryedit.html', {'form': form})

def library_delete(request, id):
    library = get_object_or_404(Library, id=id)
    library.delete()
    return redirect('library_view')
