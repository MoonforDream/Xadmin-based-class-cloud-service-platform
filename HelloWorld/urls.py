"""HelloWorld URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from classy.views import page400,page403,page404,page500
from django.conf.urls import url
from django.views import static
from django.conf import settings

handler404=page404
handler400=page400
handler403=page403
handler500=page500


urlpatterns = [
    path('admin/', admin.site.urls),
    path('class/',include('classy.urls')),
    url(r"^static/(?P<path>.*)$", static.serve, {"document_root": settings.STATIC_ROOT}, name='static'),
]
