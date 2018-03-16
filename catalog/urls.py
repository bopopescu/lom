from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, name='logout'),

    url(r'^ajax/tasks/$', views.get_tasks, name='get_tasks'),
    url(r'^ajax/nextstudent/', views.get_next_student, name='get_next_student'),
    url(r'^ajax/addsession/', views.add_session, name='add_session'),
    url(r'^viewsession/(\d+)', views.get_view_session, name='get_view_session'),
    url(r'^session/(\d+)', views.get_session, name='get_session'),
    url(r'^$', views.index, name='index'),
]