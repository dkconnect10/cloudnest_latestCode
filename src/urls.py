from django.contrib import admin
from django.urls import path,include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.shortcuts import redirect
from rest_framework_simplejwt.authentication import JWTAuthentication


schema_view = get_schema_view(
    openapi.Info(
        title="CloudNest API",
        default_version='v1',
        description="Hospital Management APIs - Swagger Docs",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="dilipkumarconnect@gmail.com"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
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
