# Create your views here.
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader, RequestContext
from django.shortcuts import render, get_object_or_404, get_list_or_404, render_to_response
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from django.views.generic.base import TemplateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import views as auth_views
from django.contrib.auth import login, authenticate
from .forms import *
from .models import Lesson, Entry, Question, Choice



class HomePageView(TemplateView):
    template_name = 'home.html'
    def get_context_data(self, **kwargs):        context = super(HomePageView, self).get_context_data(**kwargs)        return context

class ResourcePageView(TemplateView):
    template_name = 'resources/resources.html'
    def get_context_data(self, **kwargs):
        context = super(ResourcePageView, self).get_context_data(**kwargs)
        return context

class AboutUsPageView(TemplateView):
    template_name = 'about/AboutUs.html'
    def get_context_data(self, **kwargs):
        context = super(AboutUsPageView, self).get_context_data(**kwargs)
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


def register_page(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/')
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form})

@login_required
def logged_in(request):
    try:
        redirect_to = request.GET.get('next', '/')
    except ValueError:
        redirect_to = "/"
    return HttpResponseRedirect(redirect_to)


def index(request):
    latest_lesson_list = Lesson.objects.order_by('-lesson_id')
    context = {'latest_lesson_list': latest_lesson_list}
    return render(request, 'lessons/index.html', context)


def detail(request, lesson_id):
    lesson = get_object_or_404(Lesson, pk=lesson_id)
    return render(request, 'lessons/detail.html', {'lessons': lesson})


def details(request, lesson_id):
    lesson = get_object_or_404(Lesson, pk=lesson_id)
    return render(request, 'lessons/exercise/exercise.html', {'lessons': lesson})


def detailss(request, lesson_id):
    lesson = get_object_or_404(Lesson, pk=lesson_id)
    return render(request, 'lessons/quiz/quiz.html', {'lessons': lesson})
