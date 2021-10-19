
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from rest_framework.schemas import get_schema_view
from rest_framework.documentation import include_docs_urls



urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/user/',include('users.urls')),
    path('admin/', admin.site.urls),
    path('docs/', include_docs_urls(title='Starter Template')),
    path('schema/', get_schema_view(
        title="Starter Template API",
        description="Starter Template",
        version="1.0.0"
    ), name='openapi-schema'),
]
