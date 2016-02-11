'''
^ for beginning of the text
$ for end of text
\d for a digit
+ to indicate that the previous item should be repeated at least once
() to capture part of the pattern
'''
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),
]