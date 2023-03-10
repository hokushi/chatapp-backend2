from django.db import models

# Create your models here.

class ChatappUser(models.Model):
    name = models.CharField(max_length=50)  # models.XXXFieldは文字とか数字とかの型の指定

class ChatappMessage(models.Model):
    message = models.TextField()  
    sendername = models.ForeignKey(
        ChatappUser, on_delete=models.PROTECT, related_name="messages")  # 逆参照のための名前   
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(
        auto_now=True)
