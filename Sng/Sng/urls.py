from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Sng.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$','SngBlog.views.home', name = 'home'),
    url(r'^add/$', 'SngBlog.views.add', name='add'),
    url(r'^userInfo/', 'SngBlog.views.userInfo', name='userInfo'),
    url(r'^add/(\d+)/(\d+)/$', 'SngBlog.views.add2', name='add2'),
    url(r'^addAuthor/$', 'SngBlog.views.addUser', name='addUser'),
)
