from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^home$', views.get_address),
    url(r'^api/get_address$', views.get_address),
    url(r'^api/find_closest$', views.find_closest)
]