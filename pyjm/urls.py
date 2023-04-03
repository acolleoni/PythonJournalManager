from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from pyjm import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('usermanager.urls')),
    path('issues/', include('journalissues.urls')),
    path('calls/', include('proposals.urls'))
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)