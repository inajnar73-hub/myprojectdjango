from django.urls import path
from .views import *

urlpatterns = [
    path('students/create/', StudentCreate.as_view()),
    path('students/', StudentList.as_view()),
    path('students/update/<int:pk>/', StudentUpdate.as_view()),
    path('students/delete/<int:pk>/', StudentDelete.as_view()),
]