from django.db import models

class ActivityTracking(models.Model):
    is_deleted = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Test(ActivityTracking):
    name = models.CharField(max_length=500)
    question = models.CharField(max_length=5000)
    answer = models.CharField(max_length=5000)

    def __str__(self):
        return self.name

