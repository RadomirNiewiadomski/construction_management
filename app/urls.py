from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/schema/', SpectacularAPIView.as_view(), name='api-schema'),
    path(
        'api/docs/',
        SpectacularSwaggerView.as_view(url_name='api-schema'),
        name='api-docs',
    ),
    # User app URLs
    path('user/', include('user.urls', namespace='user')),
    # Construction management URLs
    path(
        'api/construction_management/',
        include(
            'construction_management.urls_api',
            namespace='construction_management.construction_management-api',
        ),
    ),
    # Root-level construction management app URLs
    path('', include('construction_management.urls')),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT,
    ) + static(
        settings.STATIC_URL,
        document_root=settings.STATIC_ROOT,
    )
