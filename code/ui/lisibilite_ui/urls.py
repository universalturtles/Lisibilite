"""lisibilite_ui URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.conf.urls import url
from lisibilite_ui_app import views as ui_view
# from lisibilite_api_app import views as api_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', ui_view.HomePageView.as_view(), name='home'),
    path('userinput', ui_view.UserInputPageView.as_view(), name='userinput'),
    path('displaymetrics', ui_view.DisplayScoresPageView.as_view(), name='displaymetrics'),
    # path('api/v1/readability', api_view.LisibiliteAPIView.as_view(), name='readabilityAPI')
]
