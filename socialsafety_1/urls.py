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