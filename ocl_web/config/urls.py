# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.views.generic import TemplateView

from apps.ocl_search.views import HomeSearchView
from apps.orgs.views import OrgDetailView

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

    # Detail
    url(r'^concept/$',
        TemplateView.as_view(template_name='pages/concept.html'),
        name="concept"),


    ######### Sources
    # List


    ######### Orgs
    # List
    url(r'^orgs/', include('apps.orgs.urls')),


    ######### Concepts
    # List

    # Detail
#    url(r'^/(?P<owner_type>[a-zA-Z0-9\-\.]+)/(?P<owner>[a-zA-Z0-9\-\.]+)/sources/(?P<source>[a-zA-Z0-9\-\.]+)/concepts/(?P<concept_name>[a-zA-Z0-9\-\.]+)/$',
#        OrgDetailView.as_view(),
#        name="org_detail"),


    ######### Users
    # List


    ######### Search
    url(r'^search/$', HomeSearchView.as_view(), name="search"),


    ######### Misc Pages (some to be moved into Dynamic views later)
    url(r'^$',
        TemplateView.as_view(template_name='pages/home.html'),
        name="home"),
    url(r'^about/$',
        TemplateView.as_view(template_name='pages/about.html'),
        name="about"),
    url(r'^features/$',
        TemplateView.as_view(template_name='pages/features.html'),
        name="features"),
    url(r'^plans/$',
        TemplateView.as_view(template_name='pages/plans.html'),
        name="plans"),
    url(r'^contact/$',
        TemplateView.as_view(template_name='pages/contact.html'),
        name="contact"),
    url(r'^api/$',
        TemplateView.as_view(template_name='pages/api.html'),
        name="api"),
    url(r'^explore/$',
        TemplateView.as_view(template_name='pages/explore.html'),
        name="explore"),
    url(r'^help/$',
        TemplateView.as_view(template_name='pages/help.html'),
        name="help"),
    url(r'^org/$',
        TemplateView.as_view(template_name='pages/org.html'),
        name="org"),
    url(r'^user/$',
        TemplateView.as_view(template_name='pages/user.html'),
        name="user"),
    url(r'^source/$',
        TemplateView.as_view(template_name='pages/source.html'),
        name="source"),
    url(r'^collection/$',
        TemplateView.as_view(template_name='pages/collection.html'),
        name="collection"),
    url(r'^new_org/$',
        TemplateView.as_view(template_name='pages/new_org.html'),
        name="new_org"),
    url(r'^new_source/$',
        TemplateView.as_view(template_name='pages/new_source.html'),
        name="new_source"),
    url(r'^new_collection/$',
        TemplateView.as_view(template_name='pages/new_collection.html'),
        name="new_collection"),
    url(r'^new_concept/$',
        TemplateView.as_view(template_name='pages/new_concept.html'),
        name="new_concept"),


    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    # User management
    url(r'^users/', include("users.urls", namespace="users")),
    url(r'^accounts/', include('allauth.urls')),

    # Uncomment the next line to enable avatars
    url(r'^avatar/', include('avatar.urls')),

    # Your stuff: custom urls go here

) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
