"""
URL configuration for managers project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path, include, re_path

from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView
from rest_framework.documentation import include_docs_urls
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView

schema_view = get_schema_view(
    openapi.Info(
        title="password-manager API",
        default_version="v1",
        description="password-manager API",
        terms_of_service="https://fairy.host/",
        contact=openapi.Contact(email="fairylandfuture@outlook.com"),
        license=openapi.License(name="AGPL-3.0"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path("favicon.ico", RedirectView.as_view(url="static/favicon.ico")),
    # 基于Django Rest Framework的API文档
    path("docs/drf-docs/", include_docs_urls(title="API Interface Documentation.")),
    # 基于drf_yasg的API文档
    path("docs/swagger/", schema_view.with_ui("swagger", cache_timeout=0), name="docs-swagger-ui"),
    path("docs/redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="docs-redoc"),
    re_path(r"^docs/swagger(?P<format>\.json|\.yaml)$", schema_view.without_ui(cache_timeout=0), name="docs-swagger-schema-json|yaml"),
    # 基于drf_spectacular的API文档
    # path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    # path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    # path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
    # django admin
    # path("admin/", admin.site.urls),
    # Apps
    path("api-example/", include("apps.example.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS)
