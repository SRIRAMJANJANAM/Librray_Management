"""
URL configuration for library_management_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from testapp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('list/', views.student_view, name='student_view'),
    path('', views.student_input, name='student_add'),
    path('students/edit/<int:id>/', views.student_input, name='student_edit'),  
    path('students/delete/<int:id>/', views.student_delete, name='student_delete'), 
    path('books/', views.book_view, name='book_view'),
    path('book/', views.book_input, name='book_add'),
    path('books/edit/<int:id>/', views.book_input, name='book_edit'), 
    path('books/delete/<int:id>/', views.book_delete, name='book_delete'), 
    path('libraries/', views.library_view, name='library_view'),
    path('library/', views.library_input, name='library_add'),
    path('libraries/edit/<int:id>/', views.library_input, name='library_edit'), 
    path('libraries/delete/<int:id>/', views.library_delete, name='library_delete'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)