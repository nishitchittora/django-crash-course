from django.shortcuts import render
from django.views import View
from crash_course.models import CrashCourse, CourseChapter, ChapterSection
from django.http import JsonResponse
from .serializers import CrashCourseSerializer, CourseChapterSerializer, \
                            ChapterSectionListSerializer, ChapterSectionDetailSerializer
# Create your views here.

class CrashCourseList(View):
    def get(self, request):
        queryset = CrashCourse.objects.all()
        serializer_data = CrashCourseSerializer(queryset, many=True).data
        return JsonResponse({'crash_course': serializer_data})


class CourseChapterList(View):
    def get(self, request, course_slug):
        queryset = CourseChapter.objects.filter(course__slug=course_slug)
        serializer_data = CourseChapterSerializer(queryset, many=True).data
        return JsonResponse({'course_chapter': serializer_data})


class ChapterSectionList(View):
    def get(self, request, course_slug, chapter_slug):
        chapter = CourseChapter.objects.filter(slug=chapter_slug, course__slug=course_slug).first()
        queryset = chapter.chaptersection_set.all()
        serializer_data = ChapterSectionListSerializer(queryset, many=True).data
        return JsonResponse({'chapter_section': serializer_data})


class SectionContentList(View):
    def get(self, request, course_slug, chapter_slug, section_slug):
        chapter = CourseChapter.objects.filter(slug=chapter_slug, course__slug=course_slug).first()
        queryset = chapter.chaptersection_set.filter(slug=section_slug)
        serializer_data = ChapterSectionDetailSerializer(queryset).data
        return JsonResponse({'section_content': serializer_data})
