# <<<<<< HEAD
from django.urls import path 
from socialsafety_1 import views
urlpatterns = [
    path("Home/",views.Home),
    path("login/",views.login),
    path("contacts/",views.contact),
    path("signup/",views.signup),
    path("dashboard/",views.dashboard),
    path("profile/",views.profile),
    path("report/",views.report),
]
#=======
from django.urls import path
from . import views
# >>>>>>> c9f1bf4e34cc4f970d9e4fe5975abd795d3c079c

urlpatterns = [
    path("", views.login_view, name="login"),

    path("Home/", views.Home, name="Home"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("logout/", views.logout_view, name="logout"),

    path("contacts/", views.contact, name="contacts"),
    path("signup/", views.signup, name="signup"),
    path("profile/", views.profile, name="profile"),
    path("report/", views.report, name="report"),
    path("location/",views.location),

]