import requests

from .models import Quiz
from .serializers import QuizSerializer

def replacing_duplicate_questions(data, object_to_save):
    """This method replaces duplicate questions"""
    
    is_a_base = True        
    while is_a_base:
        new_query = f"https://jservice.io/api/random?count=1"
        new_response = requests.get(new_query)
        new_data = new_response.json()[0]
        new_object_to_save = {
            'id': data.get('id'),
            'question': data.get('question'),
            'answer': data.get('answer'),
            'created_at': data.get('created_at'),
            'previous_question': latest_question
        }
        
        new_existing_record = Quiz.objects.filter(question=new_object_to_save.get('question')).first()

        if not new_existing_record:
            latest_question = object_to_save.get('question')
            serializer = QuizSerializer(data=object_to_save)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            is_a_base = False

def saving_the_quiz_to_the_database(data):
    """This method replaces duplicate questions"""
    
    latest_question = None
    
    for item in data:
        object_to_save = {
            'id': item.get('id'),
            'question': item.get('question'),
            'answer': item.get('answer'),
            'created_at': item.get('created_at'),
            'previous_question': latest_question
        }
        
        existing_record = Quiz.objects.filter(question=object_to_save.get('question')).first()  # Looking for duplicates of the current question
        
        if existing_record:
            replacing_duplicate_questions(data, object_to_save)
                    
        else:
            latest_question = object_to_save.get('question')
            serializer = QuizSerializer(data=object_to_save)
            serializer.is_valid(raise_exception=True)
            serializer.save()

    latest_record = Quiz.objects.latest('time_update')
    
    return latest_record.previous_question