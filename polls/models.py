from django.db import models

# Create your models here.
class question(models.Model):
    question_text = models.CharField(max_length=100)
    pub_date = models.DateTimeField('Date published')

    def __str__(self):
          return self.question_text

class choice(models.Model):
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    question = models.ForeignKey(question, on_delete=models.CASCADE)

    def __str__(self):
        return self.choice_text