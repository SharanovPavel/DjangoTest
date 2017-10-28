from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^send/$', views.mail_admins, name='mail_admins'),
]
