from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Skill(models.Model):
    name = models.CharField(max_length=20)
    skill_type = models.CharField(max_length=20)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Prompt(models.Model):
    PROMPT_TYPES = (
        ('initial', 'InitialPrompt'),
        ('enhance', 'EnhancePrompt'),
        ('follow', 'FollowUpPrompt'),
        ('custom', 'CustomPrompt'),
    )
    message = models.CharField(max_length=255)
    prompt_type = models.CharField(max_length=8, choices=PROMPT_TYPES)
    created_at = models.DateTimeField(auto_now_add=True)



class PromptMessage(models.Model):
    ROLE_CHOICES = (
        ('user', 'user'),
        ('model', 'model'),
    )
    role = models.CharField(max_length=5, choices=ROLE_CHOICES)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    part = models.ForeignKey(Prompt, on_delete=models.CASCADE)
