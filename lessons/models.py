from __future__ import unicode_literals

from django.db import models
from django.utils.html import format_html
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

class Lesson(models.Model):
    name = models.CharField(max_length=100)
    lesson_id = models.IntegerField()
    pub_date = models.DateTimeField('date published')
    user = models.ForeignKey(User)
    def __str__(self):
        return self.name
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'

class Entry(models.Model):
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    lesson_header = models.CharField(max_length=100)
    lesson_text = models.TextField()
    mod_date = models.DateField()
    def __self__(self):
        return self.lesson_header

class Question(models.Model):
    question_text = models.TextField()
    pub_date = models.DateTimeField('date published')
    lesson_num = models.IntegerField()
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    answer = models.TextField()
    hint = models.TextField()
    score = models.IntegerField()
    def __str__(self):
        return self.question_text
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'

class Quiz(models.Model):
    question_text = models.TextField()
    pub_date = models.DateTimeField('date published')
    lesson_num = models.IntegerField()
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    answer = models.TextField()
    score = models.IntegerField()
    def __str__(self):
        return self.question_text
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.TextField()
    answer = models.BooleanField()
    def __str__(self):
        return self.choice_text

class Choice2(models.Model):
    question = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    choice_text = models.TextField()
    answer = models.BooleanField()
    def __str__(self):
        return self.choice_text
