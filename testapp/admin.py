from django.contrib import admin
from testapp.models import *
# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id','name','Class','photo','video']
admin.site.register(Student,StudentAdmin)



class BookAdmin(admin.ModelAdmin):
    list_display = ['id','name','author','publication','year']
admin.site.register(Book,BookAdmin)

class LibraryAdmin(admin.ModelAdmin):
    list_display = ['id','studentname','bookname','start_date','end_date']
admin.site.register(Library,LibraryAdmin)