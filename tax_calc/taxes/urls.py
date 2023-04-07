from django.urls import path
from . import views

app_name = "taxes"

urlpatterns = [
    path("catalog/", views.index, name="index"),
    path("register", views.register_request, name="register"),
    path("login", views.login_request, name="login"),
    # path("logout", views.logout_view, name='base'),
    path("base", views.baseView, name="base"),
]