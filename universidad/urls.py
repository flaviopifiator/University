from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static, serve
from django.views.generic import RedirectView

from apps.core import admin
from apps.user.admin import admin_user


urlpatterns = [
    path('', RedirectView.as_view(url='/admin/general/')),   
    path('admin/user/', admin_user.urls),
    path('admin/general/', admin.admin_general.urls),
    path('tinymce/', include('tinymce.urls')),

    
    # Endpoint to apis.
    path('api-auth/', include('rest_framework.urls')),
    path('api/v1/', include('apps.core.urls_api', namespace='api-v1')),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
