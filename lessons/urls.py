from django.conf.urls import url

from . import views

app_name = 'lessons'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^exercise/(?P<pk>[0-9]+)/$', views.QuestionDetail.as_view(), name='details'),
    url(r'^quiz/(?P<pk>[0-9]+)/$', views.QuizDetail.as_view(), name='detailss'),
]
