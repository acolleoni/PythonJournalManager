from django.contrib import admin
from django.urls import path, include

import journalissues.urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('issues/', include('journalissues.urls')),
]
