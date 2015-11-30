from django.conf.urls import url

from . import views

# url patters to follow and which view to call

urlpatterns = [
    url(r'^$', views.render_index,),
    url(r'^api/find_closest$', views.find_closest)
]