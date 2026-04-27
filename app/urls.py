from django.urls import path
from .views import (
    home, studentlist, courselist, register, enrolledlist,
    StudentListView, StudentDetailView
)

urlpatterns = [
    path('', home),
    path('studentlist/', studentlist),
    path('courselist/', courselist),
    path('register/', register),
    path('enrolledlist/', enrolledlist),

    path('students/', StudentListView.as_view(), name='student_list'),
    path('student/<int:pk>/', StudentDetailView.as_view(), name='student_detail'),
]