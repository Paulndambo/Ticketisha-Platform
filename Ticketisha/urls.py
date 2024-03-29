from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("apps.core.urls")),
    path("accounts/", include("apps.accounts.urls")),
    path("customers/", include("apps.customers.urls")),
    path("helpdesk/", include("apps.helpdesk.urls")),
    path('tinymce/', include('tinymce.urls')),
]
urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)