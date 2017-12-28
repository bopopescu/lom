from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    url(r'^concept/$', views.get_concept, name='get_concept'),
    url(r'^work/$', views.get_tasks_group, name='get_tasks_group'),
    url(r'^ajax/tasks/$', views.get_tasks, name='get_tasks'),
    url(r'^session/(\d+)/$', views.get_session, name='get_session'),
    url(r'^$', views.index, name='index'),
]