"""
URL configuration for awn_assets_management_system project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from oauth2_provider.views import TokenView, RevokeTokenView

handler404 = "awn_assets_system.views.custom_404"
handler500 = "awn_assets_system.views.custom_500"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('oauth/', include('oauth2_provider.urls', namespace="oauth2_provider")),
    path('oauth/token/', TokenView.as_view(), name='token'),
    path('oauth/revoke_token/', RevokeTokenView.as_view(), name='revoke-token'),
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
    path('api/', include('api.urls')),
    path('', include('awn_assets_system.urls', namespace="en")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += i18n_patterns(
    path('', include('awn_assets_system.urls', namespace="ar")),
)
