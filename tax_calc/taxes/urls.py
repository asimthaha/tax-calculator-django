from django.urls import path
from . import views

app_name = "taxes"

urlpatterns = [
    path("", views.index_requestView, name="index"),
    path("register", views.register_requestView, name="register"),
    path("login", views.login_requestView, name="login"),
    # path("logout", views.logout_view, name='base'),
    path("base", views.base_requestView, name="base"),
    path("saved_records",views.saved_recordsl_requestView, name="saved_records")
]