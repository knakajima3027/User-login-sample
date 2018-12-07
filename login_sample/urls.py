from django.conf.urls import url
from django.contrib import admin
from accounts import views
from django.contrib.auth.views import login, logout

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index, name='index'),
    url(r'^create/$', views.create_account, name='create_account'),
    url(r'^login/$', views.account_login, name='login'),
    url(r'^logout/$', logout, {'template_name': 'index.html'}, name='logout'),
]
