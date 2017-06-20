from django.conf.urls import url
from .views import signup,IndexView
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^signup/$', signup, name='signup'),
    url(r'^home/$', IndexView.as_view(), name='home'),
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': 'login'}, name='logout'),

]
