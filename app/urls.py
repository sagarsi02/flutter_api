from .views import createuser, login
# from django.conf.urls import url
from django.urls import re_path

urlpatterns = [
    # path('createuser/', views.CreateUser, name='CreateUser')
    re_path(r'createuser', createuser.as_view(), name='createuser'),
    re_path(r'login', login.as_view(), name='login')
]
