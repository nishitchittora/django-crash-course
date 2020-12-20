from django.urls import path
from crash_course import views

urlpatterns = [
    path('courses', views.CrashCourseList.as_view()),
    path('course/<str:course_slug>/chapters', views.CourseChapterList.as_view()),
    path('course/<str:course_slug>/chapter/<str:chapter_slug>/sections', views.ChapterSectionList.as_view()),
    path('course/<str:course_slug>/chapter/<str:chapter_slug>/section/<str:section_slug>', views.SectionContentList.as_view()),
]
