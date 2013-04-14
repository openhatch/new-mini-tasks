from django.conf.urls import patterns, include, url

import tasks.views

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'minitasks.views.home', name='home'),
    # url(r'^minitasks/', include('minitasks.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^$', tasks.views.TaskIndex.as_view()),
    url(r'^tasks/$', tasks.views.TaskData.as_view(),
        name='tasks-data'),
    url(r'^claim/$', tasks.views.ClaimTask.as_view(),
        name='tasks-claim'),
)
