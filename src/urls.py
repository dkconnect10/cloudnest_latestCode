from django.contrib import admin
from django.urls import path,include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.shortcuts import redirect


schema_view = get_schema_view(
   openapi.Info(
      title="My Project API",
      default_version='v1',
      description="API documentation for My Project",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="your@email.com"),
      license=openapi.License(name="MIT License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)






urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/api/',include('apps.users.urls')),
    path('doctors/api/',include('apps.doctors.urls')),
    path('hospital/api/',include('apps.hospital.urls')),
    
    
    
    # swagger Api
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('', lambda request: redirect('/swagger/')),
]
