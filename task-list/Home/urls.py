from django.contrib import admin
from django.urls import path
from Home import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home, name="indexPage"),
    path('add/', views.addwork, name="addwork"),
    path('edit/<int:number>', views.edit, name="edit"),
    path('submitedit/<int:number>', views.submitedit, name="edit"),
    path('delete/<int:number>', views.delete, name="delete"),
    path('addwork/',views.stor, name="stor"),
    path('details/<int:number>', views.details, name="details"),
    path('addcolor/<int:number>/<int:colornumber>', views.addcolor, name="addcolor"),
    path('selectedColor/<int:number>', views.selectedColor, name="selectedColor"),
    path('checkbox/<int:number>/<int:datanumber>', views.checkbox, name="chekbox"),
    path("login/", views.login, name="login"),
    path("register/", views.register, name="register"),
    path("logout/", views.logout, name="logout")
]
