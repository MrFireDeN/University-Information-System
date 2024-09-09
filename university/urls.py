from django.urls import path
from . import views

urlpatterns = [
    path('api/students/', views.get_students, name='get_students'),
    path('api/instructors/', views.get_instructors, name='get_instructors'),
    path('api/dissertations/', views.get_dissertations, name='get_dissertations'),
    path('api/departments/', views.get_departments, name='get_departments'),
    path('api/instructors-by-subject/', views.get_instructors_by_subject, name='get_instructors_by_subject'),
    path('api/instructors-by-activity/', views.get_instructors_by_activity, name='get_instructors_by_activity'),
    path('api/exam-results/', views.get_exam_results, name='get_exam_results'),
    path('api/session-results/', views.get_session_results, name='get_session_results'),
    path('api/examiners/', views.get_examiners, name='get_examiners'),
    path('api/grades-by-instructor/', views.get_grades_by_instructor, name='get_grades_by_instructor'),
    path('api/thesis-topics/', views.get_thesis_topics, name='get_thesis_topics'),
    path('api/thesis-supervisors/', views.get_thesis_supervisors, name='get_thesis_supervisors'),
    path('api/instructor-load/', views.get_instructor_load, name='get_instructor_load'),
]
