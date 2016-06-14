from django.conf.urls import url, include

from . import endpoints

v1_patterns = [
    url(r'^get/user/(?P<user_id>[0-9]+)/', endpoints.get_user),
    url(r'^get/profiles/$', endpoints.get_profiles),
    url(r'^get/profile/(?P<profile_id>[0-9]+)/$', endpoints.get_profile),
    url(r'^get/names_dict/$', endpoints.get_names_dict),
]

urlpatterns = [
    url(r'^v1/', include(v1_patterns)),
]
