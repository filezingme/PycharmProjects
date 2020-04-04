from django.urls import path
from . import views

app_name = "login"
urlpatterns = [
    path('', views.LoginClass.as_view(), name = 'index'),
    path('login/', views.LoginClass.as_view(), name = 'login'),
    path('user-view/', views.ViewUser.as_view(), name = 'user-view'),
    path('view-pro/', views.view_product, name = 'view-product'),
    path('add-post/', views.AddPost.as_view(), name = 'add_post')
]
