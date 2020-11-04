# Copyright 2020 David Boyd, all rights reserved
# Program: urls.py
# Description:
#     urls.py is responsible for accepting and redistributing
#     incoming HTTP requests via views.py
# Date: 2020-10-31
# Revised:

from django.urls import path
from . import views

app_name = 'Articles'
# urlpattersn: State the names of your directories
urlpatterns = [
    # views.index: **calls index() from views.py**
    # to be -exec ::> creating some output response for HTTP request.
    path('', views.index, name='index'),
    # an example: dir = archive; fns = main
    # path('archive/', views.main, name ='main')
]

