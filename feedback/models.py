from django.db import models
from django.contrib.auth.models import User
from config.mixin.models import UserTimeStampMixin


class Feedback(UserTimeStampMixin):
    good = models.TextField()
    bad = models.TextField()
    need_improvement = models.TextField()
    created_for = models.ForeignKey(User, on_delete=models.CASCADE)
    is_anonymous = models.BooleanField(default=False)

    def __str__(self):
        return str(self.created_for.first_name)

