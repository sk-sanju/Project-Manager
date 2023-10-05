from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name=""),
    path('register',views.register, name="register"),
    path('my-login', views.my_login, name="my-login"),
    path('user-logout',views.user_logout,name="user-logout"),
    # CRUD
    path('dashboard', views.dashboard, name="dashboard"),
    path('create-records',views.create_record, name="create-records"),
    path('update-record/<int:pk>',views.update_record,name="update-record"),
    path('record/<int:pk>', views.singular_record, name="record"),
    path('delete-records/<int:pk>', views.delete_record, name="delete-records")
]
