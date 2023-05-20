from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Research(models.Model):
    title = models.CharField(max_length=100)
    issue = models.CharField(max_length=100)
    doc = models.URLField()
    field = models.ForeignKey("Interest", on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Interest(models.Model):
    interests = (
        ("Physics", "Physics"),
        ("Math", "Math"),
        ("Tech", "Tech")
    )
    interest = models.CharField(choices=interests, max_length=10)

    def __str__(self):
        return self.interest


class Report(models.Model):
    reporter = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.ForeignKey(Research, on_delete=models.CASCADE)

    def __str__(self):
        return self.reporter.username
