from django.contrib.auth.models import User
from django.db import models

from datetime import datetime

class Task(models.Model):

    PENDING = 0
    COMPLETED = 1
    STATUS = (
        (PENDING, 'Pending'),
        (COMPLETED, 'Completed'),
    )

    LOW = 1
    MEDIUM = 2
    HIGH = 3
    PRIORITY =(
        (LOW, 'Low'),
        (MEDIUM, 'Medium'),
        (HIGH, 'High'),
    )

    title = models.CharField(max_length=255)
    description = models.TextField(max_length=4000)
    slug = models.SlugField(max_length=255, null=True, blank=True)
    status = models.IntegerField(choices=STATUS, default=PENDING)
    priority = models.IntegerField(choices=PRIORITY, default=MEDIUM)
    user = models.ForeignKey(User)
    create_time = models.DateTimeField(default=datetime.now)
    deadline = models.DateTimeField(null=True)

    def __str__(self):
        return self.title