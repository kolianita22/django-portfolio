from mysite import views
from django.urls import path

urlpatterns = [
    path('home/', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('resume/', views.resume, name='resume'),
    path('project/', views.project, name='project'),
    path('contact/', views.contact, name='contact'),
]