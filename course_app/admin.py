from django.contrib import admin
from .models import *


class What_to_learnTabularInline(admin.TabularInline):
    model = What_to_learn


class RequirementsTabularInline(admin.TabularInline):
    model = Requirements


class VideoTabularInline(admin.TabularInline):
    model = Video


class CourseAdmin(admin.ModelAdmin):
    inlines = (What_to_learnTabularInline, RequirementsTabularInline, VideoTabularInline)


# Register your models here.

admin.site.register(Category)
admin.site.register(Course, CourseAdmin)
admin.site.register(Author)
admin.site.register(What_to_learn)
admin.site.register(Requirements)
admin.site.register(Lesson)
admin.site.register(Video)
admin.site.register(User_course)
admin.site.register(ProductReview)
