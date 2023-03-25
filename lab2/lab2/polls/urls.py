from django.urls import path
from polls.views import showAllQuestions, showQuestion, up_vote, down_vote, create_question, delete_question, update_question
urlpatterns = [
    path('polls/', showAllQuestions, name='polls'),
    path('polls/<int:id>', showQuestion, name='question_details'),
    path('polls/create', create_question, name='create_question'),
    path('polls/delete/<int:id>', delete_question, name='delete_question'),
    path('polls/update/<int:id>', update_question, name='update_question'),
    path('polls/up/<int:q_id>/<int:user_id>', up_vote, name='up_vote'),
    path('polls/down/<int:q_id>/<int:user_id>', down_vote, name='down_vote'),
]
