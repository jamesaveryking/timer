from django.db import models

# Create your models here.
class User(models.Model):
    user_id = models.CharField(primary_key=True, unique=True, max_length=35)
    first_name = models.CharField(max_length=70)
    last_name = models.CharField(max_length=70)
    email_address = models.EmailField(max_length=70)
    password = models.CharField(max_length=49)
    security_question = models.CharField(max_length=70)
    security_answer = models.CharField(max_length=70)

class TimerRequest(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    timerLabel = models.CharField(max_length=70)
    start_time = models.DateTimeField(max_length=70)
    end_time = models.DateTimeField(max_length=70)
    total_time = models.DateTimeField(max_length=70)
    start_switch = models.BooleanField()
    end_switch = models.BooleanField()
    start_primer = models.BooleanField()
    end_primer = models.BooleanField()
