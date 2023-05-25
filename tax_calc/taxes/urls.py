from django.urls import path,include
from .views import *
from . import views

app_name = "taxes"

urlpatterns = [
    path("index", IndexView.as_view(), name="index"),
    path("base", BaseView.as_view(), name="base"),
    path("feedback", FeedbackView.as_view(), name="feedback"),
    path("del_records", DeleteRecordsView.as_view(), name="del_records"),
    path("saved_records", SavedRecordsView.as_view(), name="saved_records"),
    path("register", RegisterView.as_view(), name="register"),
    path("", LoginRequestView.as_view(), name="login"),
    path("logout", LogoutView.as_view(), name="logout"),
]