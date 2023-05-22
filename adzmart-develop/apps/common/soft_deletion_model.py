from django.db import models
from django.utils import timezone

from adzmart.base_model import BaseModel


class SoftDeletionQueryset(models.QuerySet):
    def delete(self, hard=False):
        if hard:
            return super().delete()
        return self.update(deleted_at=timezone.now())


class SoftDeletionManager(models.Manager):
    def get_queryset(self):
        return SoftDeletionQueryset(self.model, using=self._db)


class ActiveObjectsManager(SoftDeletionManager):
    def get_queryset(self):
        return super().get_queryset().filter(deleted_at__isnull=True)


class SoftDeletionModel(BaseModel):
    deleted_at = models.DateTimeField(blank=True, null=True)
    objects = SoftDeletionManager()
    active_objects = ActiveObjectsManager()

    class Meta:
        abstract = True

    def delete(self, hard=False):
        if hard:
            return super().delete()

        self.deleted_at = timezone.now()
        self.save()
