from django.contrib import admin
from .models import Question, Choice, Submission, Course, Lesson, Instructor, Enrollment


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionInline(admin.TabularInline):
    model = Question
    extra = 1
    inlines = [ChoiceInline]


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question', 'grade')
    inlines = [ChoiceInline]


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('title', 'course')
    inlines = [QuestionInline]


admin.site.register(Choice)
admin.site.register(Submission)
admin.site.register(Course)
admin.site.register(Instructor)
admin.site.register(Enrollment)
