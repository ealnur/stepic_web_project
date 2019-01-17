from django.conf.urls import url

from qa.views import test, post_list_all

urlpatterns = [
  url(r'^\w+$', post_list_all, name='post-list-all'),
]


