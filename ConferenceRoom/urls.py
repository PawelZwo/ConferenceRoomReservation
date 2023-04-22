"""
URL configuration for ConferenceRoom project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
import conference.views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', conference.views.Index.as_view()),
    path('room/new', conference.views.AddRoom.as_view()),
    path('room/', conference.views.List.as_view()),
    path('room/details/<int:id>', conference.views.Details.as_view()),
    path('room/modify/<int:id>', conference.views.Modify.as_view()),
    path('room/delete/<int:id>', conference.views.Delete.as_view()),
    path('room/reserve/<int:id>', conference.views.Reserve.as_view()),
]
