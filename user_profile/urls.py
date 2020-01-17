from django.urls import  re_path
from .views import *


urlpatterns = [
    # api
    re_path(r'^api/v1/profile/$', user_profile_collection, name='user_profile_collection'),
    re_path(r'^api/v1/profile/(?P<pk>[0-9]+)$', user_profile_element, name='user_profile_element'),
    re_path(r'^api/v1/post/profile/$', HelloView.as_view(), name='post_user_profile')
]