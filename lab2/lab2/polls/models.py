from django.db import models
from django.db.models import Sum
# Create your models here.


class Votes(models.Model):
    question_id = models.IntegerField(default=0)
    user_id = models.IntegerField(default=0)
    up_down = models.IntegerField(default=0)


class Questions(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateField(auto_now=False, auto_now_add=False)
    user_id = models.IntegerField(default=0)

    def votes(self):
        return Votes.objects.values('question_id').annotate(sum=Sum('up_down')).filter(question_id=self.id)

    # votes = self._votes()
