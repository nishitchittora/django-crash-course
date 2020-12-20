from rest_framework import serializers
from .models import CrashCourse, CourseChapter, ChapterSection

class CrashCourseSerializer(serializers.ModelSerializer):
    no_of_chapter = serializers.SerializerMethodField()

    class Meta:
        model = CrashCourse
        fields = ('id', 'title', 'slug', 'no_of_chapter')

    def get_no_of_chapter(self, obj):
        return obj.coursechapter_set.count()


class CourseChapterSerializer(serializers.ModelSerializer):

    class Meta:
        model = CourseChapter
        fields = ('id', 'title', 'slug', 'course')


class ChapterSectionListSerializer(serializers.ModelSerializer):

    class Meta:
        model = ChapterSection
        fields = ('id', 'title', 'slug', )


class ChapterSectionDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = ChapterSection
        fields = ('id', 'title', 'slug', 'description')
