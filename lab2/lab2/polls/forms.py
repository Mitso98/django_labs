from django import forms
from polls.models import Questions


class QuestionsForm(forms.ModelForm):
    class Meta:
        model = Questions
        fields = [('question_text')]
