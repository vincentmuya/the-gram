from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from . import views

urlpatterns=[

    url(r'^$',views.index,name ='index'),
    url(r'^post/(\d+)',views.post,name ='post'),
    url(r'^new/post/$', views.new_post, name='new-post')

]
