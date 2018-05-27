# -*- coding: utf-8 -*-
from __future__ import unicode_literals


# Create your views here.
import time

from django.utils.functional import lazy
from django.views.generic import TemplateView
from django_lare.mixins import DefaultLareViewMixin


class HomeView(DefaultLareViewMixin, TemplateView):
    lare_current_namespace = 'Site1.Home'
    template_name = 'home.html'


class Page1(DefaultLareViewMixin, TemplateView):
    def heavy_func(self):
        time.sleep(1)
        return "heavy func"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'heavy_func': lazy(self.heavy_func, str)
        })
        return context


class Page1Tab1(Page1):
    lare_current_namespace = 'Site1.Page1.Tab1'
    template_name = 'page1_tab1.html'


class Page1Tab2(Page1):
    lare_current_namespace = 'Site1.Page1.Tab2'
    template_name = 'page1_tab2.html'


class Page2(DefaultLareViewMixin, TemplateView):
    lare_current_namespace = 'Site1.Page2'
    template_name = 'page2.html'
