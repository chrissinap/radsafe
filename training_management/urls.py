from django.conf.urls import url
from training_management import views


app_name = 'training_management'

urlpatterns = [
    url(r'^$', views.profile_list, name='profile_list'),
    url(r'^(?P<pk>[\d]+)$', views.profile_detail, name='profile_detail')
]

#
# (?P<username>[\w\-]+)$