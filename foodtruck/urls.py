from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.render_index,),
    url(r'^api/find_closest$', views.find_closest)
]