# -*- coding: utf-8 -*-
"""
Created on Sat Aug  3 21:06:04 2024

@author: HackHubAfrica
"""

from django.urls import path
from . import views

app_name = 'polls'


#Use generic views: Less code is better
urlpatterns = [
    #path('', views.simple_view, name='index'),
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]



"""
The question_id=34 part comes from <int:question_id>. Using angle brackets “captures” part of the URL
and sends it as a keyword argument to the view function. The :question_id> part of the string defines the name
that will be used to identify the matched pattern, and the <int: part is a converter that determines what patterns
should match this part of the URL path.

The path() function is passed four arguments, two required: route and view, and two optional: kwargs, and
name. At this point, it’s worth reviewing what these arguments are for.
"""