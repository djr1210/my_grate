from django.conf.urls import url
from app1 import views


urlpatterns = [
    url(r'^index/',views.index),
    url(r'^create/',views.create,name='create'),
    url(r'^search/',views.search,name='search')
]