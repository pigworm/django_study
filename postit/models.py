from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Postit(models.Model):
    message = models.TextField()
    created_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, null=True, blank=True)

    def __str__(self):
        return '%s %s' %(self.id, self.message)

    def test_func(self):
        return self.created_at