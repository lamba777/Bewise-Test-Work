from django.urls import path

from .views import QuizApi, DeleteQuiz

urlpatterns = [
    path('api/v1/quiz/', QuizApi.as_view(), name='quiz'),
    path('api/v1/delete/', DeleteQuiz.as_view(), name='deletequiz')
]