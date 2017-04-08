from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from django.views.generic.base import TemplateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import views as auth_views

from .models import Lesson, Entry, Question, Choice

class HomePageView(TemplateView):
    template_name = 'home.html'
    def get_context_data(self, **kwargs):        context = super(HomePageView, self).get_context_data(**kwargs)        return context

#class LoginPageView(LoginRequiredMixin, View):
#    login_url = 'login.html'
#    redirect_field_name = 'redirect_to'

class ResourcePageView(TemplateView):
    template_name = 'resources/resources.html'
    def get_context_data(self, **kwargs):
        context = super(ResourcePageView, self).get_context_data(**kwargs)
        return context

class IndexView(generic.ListView):
    template_name = 'lessons/index.html'
    context_object_name = 'latest_lesson_list'
    def get_queryset(self):
        return Lesson.objects.order_by('lesson_id')

class DetailView(generic.DetailView):
    model = Lesson
    template_name = 'lessons/detail.html'
    def get_queryset(self):
        return Lesson.objects.order_by('lesson_id')


class QuestionDetail(generic.DetailView):
    model = Lesson
    template_name = 'lessons/exercise/exercise.html'
    def get_queryset(self):
        return Lesson.objects.order_by('lesson_id')
    #def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
    #    context = super(QuestionDetail, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the books
    #    context['Question_list'] = Question.objects.filter('lesson_num = lesson_id')
    #    return context

class QuizDetail(generic.DetailView):
    model = Lesson
    template_name = 'lessons/quiz/quiz.html'
    def get_queryset(self):
        return Lesson.objects.order_by('lesson_id')

def login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        login(request, user)
    else:
        #INVLAID LOGIN
        logout(request)
def logout(request):
    logout(request)

def index(request):
    latest_lesson_list = Lesson.objects.order_by('-lesson_id')
    context = {'latest_lesson_list': latest_lesson_list}
    return render(request, 'lessons/index.html', context)

def detail(request, lesson_id):
    lesson = get_object_or_404(Lesson, pk=lesson_id)
    return render(request, 'lessons/detail.html', {'lessons': lesson})

@login_required
def details(request, lesson_id):
    lesson = get_object_or_404(Lesson, pk=lesson_id)
    return render(request, 'lessons/exercise/exercise.html', {'lessons': lesson})

@login_required
def detailss(request, lesson_id):
    lesson = get_object_or_404(Lesson, pk=lesson_id)
    return render(request, 'lessons/quiz/quiz.html', {'lessons': lesson})
