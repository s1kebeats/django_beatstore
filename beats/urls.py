from xml.etree.ElementInclude import include
from django.conf import settings
from django.urls import path
from django.urls.conf import re_path
from django.views.generic.base import RedirectView
from . import views
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('beats/', views.BeatsListView.as_view(), name='beats'),
    path('termsofuse/', views.terms, name='terms'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)