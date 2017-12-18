"""Disc_Caddy_App URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from pages import views as page_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    # pages urls
    url(r'^$', page_views.map_search, name='map_search'),
    url(r'^register/$', page_views.register, name='register'),
    url(r'^login/$', page_views.user_login, name='login'),
    url(r'^logout/$', page_views.user_logout, name='logout'),
    url(r'^news/$', page_views.news, name='news'),
    url(r'^my_bag/$', page_views.my_bag, name='my_bag'),
    url(r'^friends/$', page_views.friends, name='friends'),
    url(r'^add_friends/$', page_views.add_friends, name='add_friends'),
    url(r'^settings/$', page_views.settings, name='settings'),
    url(r'^activity/$', page_views.activity, name='activity'),
    url(r'^api/username/$', page_views.find_username, name='username_api'),
    url(r'^api/check_in_form/$', page_views.check_in_form, name='check_in_form'),
    url(r'^api/accept_friend/$', page_views.accept_friend, name='accept_friend'),
    url(r'^api/reject_friend/$', page_views.reject_friend, name='reject_friend'),
    url(r'^profile/(?P<username>[\w-]+)/', page_views.profile, name='profile'),
    url(r'^courses/(?P<slug>[\w-]+)/', page_views.courses, name='courses'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
