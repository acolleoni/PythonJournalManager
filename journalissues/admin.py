from django.contrib import admin
from journalissues import models

admin.site.register(models.Article)
admin.site.register(models.Author)
admin.site.register(models.Issue)
admin.site.register(models.Category)