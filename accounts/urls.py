from django.urls import path
from . import views


urlpatterns = [
	path('', views.home, name='home'),
	path('products/', views.products, name='product'),
	path('customer/<str:pk_test>/', views.customer, name='customer'),
	path('create_order/<str:pk>/', views.CreateOrder, name='create_order'),
	path('update_order/<str:pk>/', views.UpdateOrder, name='update_order'),
	path('delete_order/<str:pk>/', views.deleteOrder, name='delete_order'),
	path('login/', views.loginPage, name='login'),
	path('logout/', views.logoutUser, name='logout'),
	path('register/', views.register, name='register'),
]