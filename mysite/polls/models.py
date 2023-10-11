from django.db import models


# Each model is represented by a class that subclass django.db.models.Model
# Each model has a number of class variables, each of which represents a database field in the model.
class Question(models.Model):
    # Each field is represented by an instance of a Field class.
    # The name of each Field instance is the field's name.
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField()

    def __str__(self):
        return self.choice_text
