from django.urls import path
from . import views

urlpatterns = [
    path("", views.login_view, name="login"),

    path("Home/", views.Home, name="Home"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("logout/", views.logout_view, name="logout"),

    path("contacts/", views.contact, name="contacts"),
    path("signup/", views.signup, name="signup"),
    path("profile/", views.profile, name="profile"),
    path("report/", views.report, name="report"),
]