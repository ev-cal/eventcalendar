"""eventcalendar URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from home import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.main,name="main"),
    path('about',views.about,name="about"),
    path('feedback',views.feedback,name="feedback"),
    path('eventdetails/<int:eventid>',views.eventdetails,name="eventdetails"),
    path('filter',views.filter,name="filter"),
    path('accounts/',include('accounts.urls')),
    path('delete/<int:cmtid>',views.delete,name='delete'),
    path('cancel',views.cancel,name="cancel"),
    path('deleteEvent/<int:delid>',views.eventdelete,name='eventdelete'),
    path('update/<int:upid>',views.update,name='update')

]
