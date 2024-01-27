from django.db import models

# Create your models here.
class Question(models.Model):
    q_id = models.AutoField(primary_key=True,unique=True)
    question = models.CharField(max_length=7000,default="")
    option1 = models.CharField(max_length=700,default="")
    option2 = models.CharField(max_length=700,default="")
    option3 = models.CharField(max_length=700,default="")
    option4 = models.CharField(max_length=700,default="")
    ans = models.CharField(max_length=700,default="")
    user_ans = models.CharField(max_length=700,default="")

    def __str__(self):
        return str(self.q_id)

class Question_s1(models.Model):
    q_id = models.AutoField(primary_key=True,unique=True)
    question = models.CharField(max_length=7000,default="")
    option1 = models.CharField(max_length=700,default="")
    option2 = models.CharField(max_length=700,default="")
    option3 = models.CharField(max_length=700,default="")
    option4 = models.CharField(max_length=700,default="")
    ans = models.CharField(max_length=700,default="")
    user_ans = models.CharField(max_length=700,default="")

    def __str__(self):
        return str(self.q_id)
        
