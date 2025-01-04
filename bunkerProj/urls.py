
from django.contrib import admin
from django.urls import path
from crm import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.first_page),
    path('/', views.thanks_page , name='thanks_page'),
]
