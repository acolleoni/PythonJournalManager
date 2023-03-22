from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('issues/', include('journalissues.urls')),
    path('calls/', include('proposals.urls'))
]
