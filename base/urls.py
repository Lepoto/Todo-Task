from django.urls import path
from .views import *


urlpatterns = [
    path('login/', BaseLoginView.as_view(), name="login-user"),
    path('logout/', BaseLogoutView.as_view(), name="logout-user"),
    path('register/', RegisterView.as_view(), name="register-user"),

    path('', TaskList.as_view(), name="tasks"),
    path('task/<slug:slug>', TaskDetail.as_view(), name="task-detail"),
    path('create/',TaskCreate.as_view(), name="create-task"),
    path('task/update/<slug:slug>', TaskUpdate.as_view(), name="update-task"),
    path('task/delete/<slug:slug>', TaskDelete.as_view(), name="delete-task"),
]