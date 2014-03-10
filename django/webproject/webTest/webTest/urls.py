from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'webTest.views.home', name='home'),
                       # url(r'^webTest/', include('webTest.foo.urls')),
                       url(r'^$', 'webTest.hello.index', name='hello'),
                       url(r'^webTest/hello', 'webTest.hello.index', name='hello'),

                       # Uncomment the admin/doc line below to enable admin documentation:
                       # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

                       # Uncomment the next line to enable the admin:
                       # url(r'^admin/', include(admin.site.urls)),
)
