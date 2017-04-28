from django.contrib import admin
from django.utils.safestring import mark_safe
from django.core.urlresolvers import reverse
# Register your models here.
from .models import *

class EditLinkToInlineObject(object):
    def edit_link(self, instance):
        url = reverse('admin:%s_%s_change' % (
            instance._meta.app_label,  instance._meta.model_name),  args=[instance.pk] )
        if instance.pk:
            return mark_safe(u'<a href="{u}">edit</a>'.format(u=url))
        else:
            return ''


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class Choice2Inline(admin.TabularInline):
    model = Choice2
    extra = 3

class QuizInLine(EditLinkToInlineObject, admin.TabularInline):
    model = Quiz
    inlines = [Choice2Inline]
    readonly_fields = ('edit_link',)

class QuestionInLine(EditLinkToInlineObject, admin.TabularInline):
    model = Question
    inlines=[ChoiceInline]
    readonly_fields = ('edit_link',)

class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]

class QuizAdmin(admin.ModelAdmin):
    inlines = [Choice2Inline]

class EntryInLine(admin.TabularInline):
    model = Entry

class LessonAdmin(admin.ModelAdmin):
    inlines = [EntryInLine,QuestionInLine,QuizInLine]
    list_display = ('name', 'lesson_id', 'pub_date')
    search_fields = ['name']

admin.site.register(Quiz, QuizAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Lesson, LessonAdmin)
