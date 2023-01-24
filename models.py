from django.db import models

class Feedback(models.Model):
    like_count = models.IntegerField()
    dislike_count = models.IntegerField()
