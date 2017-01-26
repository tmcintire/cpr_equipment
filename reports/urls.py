from django.conf.urls import include, url

from views import report

urlpatterns = [
    url(r'^report/$', report, name="report"),

]
