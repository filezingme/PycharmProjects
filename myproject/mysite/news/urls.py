from django.urls import path
from . import views

app_name = "news"
urlpatterns = [
    # path('', views.index, name = 'index'),
    path('', views.IndexClass.as_view(), name = 'index'),

    # path('add/', views.add_post, name='add'),
    #path('add/', views.AddClass.as_view(), name='add'),
    #path('save/', views.save_news, name='save'),

    path('save/', views.ClassSaveNews.as_view(), name='save'),

    # path('list/', views.viewlist, name='list'),
    path('list/', views.ListClass.as_view(), name='list'),

    path('email/', views.email_view, name='email'),

    path('process/', views.process, name='pro')
]
