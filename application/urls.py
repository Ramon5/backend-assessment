from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions

from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Activation Requests API",
      default_version='v1',
      description="Documentação contento as rotas da API, a utilização dos verbos http para cada rota e o eventual comportamento",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="ramon.srodrigues01@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('admin', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('', include('apps.urls')),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]
