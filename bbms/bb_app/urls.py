from . import views
from django.urls import path

app_name='bb_app'

urlpatterns=[
    path('logout/$',views.user_logout,name='user_logout'),
    path('', views.user_login, name="user_login"),
]
