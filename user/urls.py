from django.contrib import admin
from django.urls import path, include
from .views import LoginView,SignUpView


urlpatterns = [
    path('login/', LoginView.as_view({'post':'login'}),name="login"),
    path('signup/', SignUpView.as_view(),name="signup"),

]
