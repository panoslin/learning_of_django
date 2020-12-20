#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by panos on 2020/12/20
# IDE: PyCharm

from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
]