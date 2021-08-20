from django.db import models
import uuid

class Contactmessage(models.Model):
    MALE = "M"
    FEMALE = "F"

    GENDER = [
        (MALE,'Male'),
        (FEMALE,'Female')
    ]
    id = models.UUIDField(unique=True, primary_key=True,default=uuid.uuid4, editable=False)
    fullname = models.CharField(max_length=255)
    email = models.EmailField()
    subject = models.TextField(blank=True,null=True)
    gender = models.CharField(max_length=1,choices=GENDER)
    message = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)
