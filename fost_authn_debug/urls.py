from django.conf.urls import *

urlpatterns = patterns('',
    (r'^$', 'fost_authn_debug.views.root'),
    (r'^anonymous/$', 'fost_authn_debug.views.anonymous'),
    (r'^signed/$', 'fost_authn_debug.views.signed'),
)
