from django.conf.urls import url

from qa.views import test

print 3333333

urlpatterns = [
  url(r'^', test, name = 'test'),
]

print urlpatterns

