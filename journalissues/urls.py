from django.urls import path
from . import views

urlpatterns = [
    path('', views.issuesView.as_view()),
    path('<int:pk>', views.issueView.as_view())
]