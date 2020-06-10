from django.urls import path
from .api import LessonDetailAPI,CourseDetailsAPI,CourseAPI,LessonAPI,CourseCreateAPI,CourseLessonAPI

urlpatterns = [
    path('courses/',CourseAPI.as_view(),name="course_list"),
    path('courses/create/',CourseCreateAPI.as_view(),name="course_create"),
    path('courses/<pk>/',CourseDetailsAPI.as_view(),name="course_detail"),
    # path('courses/<pk>/lesson/',CourseLessonAPI.as_view(),name="course_lesson"),
    path('lesson/',LessonAPI.as_view(),name="lesson_list"),
    path('lesson/<pk>/',LessonDetailAPI.as_view(),name="lesson_detail"),
]