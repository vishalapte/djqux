from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

from qux.auth import urls as qux_auth_urls
from qux.token import urls as qux_token_urls


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(qux_auth_urls)),
    path('tokens/', include(qux_token_urls)),
]

urlpatterns += [
    path('', TemplateView.as_view(template_name='qux_default_home.html'), name='home'),
]

urlpatterns += [
    path('newsfeed/', include('community.newsfeed.urls')),
]

urlpatterns += [
    path('billing/', include('payments.urls')),
]
