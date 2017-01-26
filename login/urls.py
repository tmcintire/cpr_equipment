from django.conf.urls import include, url
from django.contrib.auth.views import password_change
from views import login, auth_view, invalid_login, logout, account, loggedin

urlpatterns = [
    url(r'^accounts/login/$', login, name="login"),
    url(r'^accounts/auth/$', auth_view, name="auth_view"),
    url(r'^accounts/logout/$', logout, name="logout"),
    url(r'^accounts/invalid/$', invalid_login, name="invalid_login"),
    url(r'^accounts/loggedin/$', loggedin, name="loggedin"),
    url(r'^accounts/user/$', account, name="account"),
    url(r'^accounts/password_change/$', 'django.contrib.auth.views.password_change', {'template_name': 'change_password.html'})


]
