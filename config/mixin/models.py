from django.db import models
from django.contrib.auth.models import User


class TimeStampMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class UserMixin(models.Model):
    created_by = models.ForeignKey(User, null=True,
                                   on_delete=models.PROTECT, related_name="%(app_label)s_%(class)s_related")

    class Meta:
        abstract = True


class UserTimeStampMixin(UserMixin, TimeStampMixin):
    pass

    class Meta:
        abstract = True
