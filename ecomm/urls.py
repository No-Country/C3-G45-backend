from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static


from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="No Country C03-G57",
      default_version='v1',
      description="API REST for No Country Ecommerce C03-G57",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="megordon@outlook.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('djoser.urls')),
    path('api/v1/', include('djoser.urls.authtoken')),
    path('api/v1/', include('products.urls')),
    path('auth/',include('authentication.urls')),
    path('auth/', include('djoser.urls.jwt')),
    #path('orders/', include('products.urls')),
    # swagger urls
    path('swagger<format>.json|.yaml/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
