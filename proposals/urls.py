from django.urls import path
from . import views

urlpatterns = [
    path('', views.callsForPapersView.as_view()),
    path('<int:pk>/', views.callForPapersView.as_view()),
    path('proposals/', views.proposalsView.as_view()),
    path('proposals/<int:pk>/', views.proposalView.as_view()),
    path('reviews/', views.reviewsView.as_view()),
    path('reviews/<int:pk>/', views.reviewView.as_view()),
    path('proposers/', views.proposersView.as_view()),
    path('proposers/<int:pk>/', views.proposerView.as_view())
]
