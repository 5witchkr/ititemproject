from django.conf.urls import url
from .views import Login, Join

urlpatterns = [
    url('login', Login.as_view(), name='login'),
    url('join', Join.as_view(), name='join'),
]
