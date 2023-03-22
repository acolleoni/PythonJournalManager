from django.urls import path
from . import views

urlpatterns = [
    path('', views.issuesView.as_view()),
    path('<int:pk>/', views.issueView.as_view()),
    path('<int:issue_id>/articles/', views.articlesView.as_view()),
    path('<int:issue_id>/articles/<int:pk>/', views.articleView.as_view()),
    path('authors/', views.authorsView.as_view()),
    path('authors/<int:pk>/', views.authorView.as_view())
]