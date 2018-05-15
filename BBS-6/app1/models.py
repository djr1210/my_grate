from django.db import models
import time
from datetime import datetime

class Post(models.Model):
    title = models.CharField(max_length=64)
    created = models.DateTimeField(auto_now_add=True)
    content = models.TextField()

