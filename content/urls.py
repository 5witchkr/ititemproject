from django.conf.urls import url
from .views import Main, CreateMain

urlpatterns = [
    url('main', Main.as_view(), name='main'),
    url('create', CreateMain.as_view(), name='create')
]
