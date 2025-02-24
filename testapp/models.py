from django.db import models
from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=50)
    Class = models.IntegerField()
    photo = models.ImageField(upload_to='images/', default='images/default.webp')
    video = models.FileField(upload_to='videos/', default='videos/default.mp4')

    def __str__(self):
        return self.name

        
class Book(models.Model):
    name = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    publication = models.CharField(max_length=120)
    year = models.DateField()

    def __str__(self):
        return self.name  


class Library(models.Model):
    studentname = models.ForeignKey(Student, on_delete=models.CASCADE)
    bookname = models.ForeignKey(Book, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return f"{self.studentname} - {self.bookname}"  
