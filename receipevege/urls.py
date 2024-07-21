from django.urls import path
from . import views

urlpatterns = [
    path('', views.loginPage, name='LoginPage'),
    path('singup/', views.singUp, name='SingUpPage'),
    path('logout/', views.logoutPage, name='LogoutPage'),
    path('receipe/', views.receipAddeMethod, name='ADD_DATA-RECEIPE'),
    path('delete/<int:id>/', views.deleteData, name='DeleteReceipe'),
    path('update/<int:id>/', views.updateData, name='UpdateData'),
]
