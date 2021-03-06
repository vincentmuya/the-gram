from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from . import views

urlpatterns=[

    url(r'^$',views.index,name ='index'),
    url(r'^new/comment/$',views.index,name='new-comment'),
    url(r'^post/(\d+)',views.post,name ='post'),
    url(r'^new/post/$', views.new_post, name='new-post'),
    url(r'^profile/$', views.update_profile, name ='profile'),
    # url(r'^edit/profile/$', views.edit_profile, name='edit-profile'),

]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
