"""django_lare_example URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django_lare_example.lare_example_core import views as core_views

urlpatterns = [
    url(r'^$', core_views.HomeView.as_view(), name='home'),
    url(r'^page1/tab1/$', core_views.Page1Tab1.as_view(), name='page1_tab1'),
    url(r'^page1/tab2/$', core_views.Page1Tab2.as_view(), name='page1_tab2'),
    url(r'^page2/$', core_views.Page2.as_view(), name='page2')
]
