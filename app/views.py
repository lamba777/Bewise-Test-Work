import requests

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Quiz
from .business_logic import saving_the_quiz_to_the_database

class DeleteQuiz(APIView):
    """Database cleanup view"""
    
    def get(self, request):
        Quiz.objects.all().delete()
        return Response({"all_the_posts_deleted"}, status=status.HTTP_200_OK)

class QuizApi(APIView):
    """View for working with quiz"""
    
    def post(self, request):
        count = request.data.get('questions_num', 1)    # number of questions
        api_url = f"https://jservice.io/api/random?count={count}"
        
        try:
            response = requests.get(api_url)
            data = response.json()
        except Exception as e:
            return Response({'error': 'Failed to retrieve data from the external API'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
        if data:
            answer = saving_the_quiz_to_the_database(data)
        
        return Response({answer}, status=status.HTTP_200_OK)