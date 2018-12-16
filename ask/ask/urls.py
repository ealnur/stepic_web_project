"""ask URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from django.conf.urls import include, url
from django.contrib import admin
from qa import views

print 22222222

urlpatterns = [
    url(r'^', include('qa.urls')),
    url(r'^admin/', admin.site.urls),
#    url(r'^login/$'),
#    url(r'^signup/$'),
#    url(r'^question/(\d+)/$', qa.views.test),
#    url(r'^ask/$'),
#    url(r'^popular/$'),
#    url(r'^new/$')
]

print urlpatterns

