from django.db import models
from .mixins import StatusMixin, TimeStampedModel, TitleSlugMixin

# Create your models here.


class CrashCourse(TimeStampedModel, StatusMixin, TitleSlugMixin):
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title


class CourseChapter(TimeStampedModel, StatusMixin, TitleSlugMixin):
    description =  models.TextField(blank=True, null=True)
    course = models.ForeignKey(CrashCourse, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.title


class ChapterSection(TimeStampedModel, StatusMixin, TitleSlugMixin):
    description =  models.TextField(blank=True, null=True)
    chapter = models.ForeignKey(CourseChapter, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.title
