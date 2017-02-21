from django.conf.urls import *
from blog.views import get_blogs, login, register, get_detail


urlpatterns = patterns('',
                       url(r'^login/register/$', register, name='register'),
                       url(r'^login/$', login, name='login'),
                       url(r'^login/blog-list/$', get_blogs,
                           name='blog_get_blogs'),
                       url(r'^detail/(\d+)/$', get_detail,
                           name='blog_get_detail'),
                       )
