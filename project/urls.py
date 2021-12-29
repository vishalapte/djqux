"""quxp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, include
from django.views.generic import TemplateView
from qux.auth import urls as qux_auth_urls
from qux.token import urls as qux_token_urls
from shorturl.urls import appurls as shorturl_urls
from shorturl.urls import apiurls as shorturl_urls_api

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(qux_auth_urls)),
    path('tokens/', include(qux_token_urls)),
]

urlpatterns += [
    path('', TemplateView.as_view(template_name='qux_default_home.html'), name='home'),
]

urlpatterns += [
    path('newsfeed/', include('newsfeed.urls')),
]
urlpatterns += [
    path('billing/', include('payments.urls')),
]

urlpatterns += [
    path('api/v1/shorturl/', include(shorturl_urls_api, namespace='qux_shorturl_api')),
    path('', include(shorturl_urls, namespace='qux_shorturl')),
]
