from django.urls import path
from feedback import views

urlpatterns = [
    path('', views.FeedbackGetList.as_view()),
    path('create/', views.FeedbackCreate.as_view()),
]