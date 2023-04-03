from django.urls import path
from . import views

urlpatterns = [
    path('', views.issuesView.as_view()),
    path('<int:pk>/', views.issueView.as_view()),
    path('<int:issue_id>/articles/', views.issueArticlesView.as_view()),
    path('last/', views.lastIssueView.as_view()),
    path('last/articles/', views.lastIssueArticlesView.as_view()),
    path('articles/', views.articlesView.as_view()),
    path('articles/<int:pk>/', views.articleView.as_view()),
    path('authors/', views.authorsView.as_view()),
    path('authors/<int:pk>/', views.authorView.as_view()),
    path('categories/', views.categoriesView.as_view()),
    path('categories/<int:pk>/', views.categoryView.as_view()),
    path('saveissuefile/', views.SaveIssueFile.as_view())

]