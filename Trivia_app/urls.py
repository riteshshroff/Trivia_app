from Trivia_app import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='home'),
    # path('create-quiz/', views.create_quiz, name='create-quiz'),
    path('start-quiz/', views.start_quiz, name='start-quiz'),
    path('view-all/', views.view_all, name='view-all'),
]
