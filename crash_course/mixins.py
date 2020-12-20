from django.db import models
from django.core.validators import RegexValidator
from ckeditor_uploader.fields import RichTextUploadingField
from django.template.defaultfilters import slugify

from .managers import StatusMixinManager


class TitleSlugMixin(models.Model):
    title = models.CharField(max_length=128, blank=True, null=True)
    slug = models.SlugField(max_length=128, blank=True, null=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(TitleSlugMixin, self).save(*args, **kwargs)

    class Meta:
        abstract = True


class StatusMixin(models.Model):
    is_active = models.BooleanField("active", default=True, blank=False, null=False)
    is_deleted = models.BooleanField("deleted", default=False, blank=False, null=False)

    objects = StatusMixinManager()

    def activate(self):
        if not self.is_active:
            self.is_active = True
            self.save()

    def deactivate(self):
        if self.is_active:
            self.is_active = False
            self.save()

    def remove(self):
        if not self.is_deleted:
            self.is_deleted = True
            self.save()

    def has_changed(self, field):
        model = self.__class__.__name__
        return getattr(self,field) != getattr(self,"_" + model + "__original_" + field)

    def save(self, *args, **kwargs):
        if self.is_deleted:
            self.is_active = False
        super(StatusMixin, self).save(*args, **kwargs)

    class Meta:
        abstract = True


class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
