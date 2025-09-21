from django.urls import path
from . import views

urlpatterns = [
    path("register/",views.admin_signup,name="admin_signup"),
    path('test/',views.test),
]
