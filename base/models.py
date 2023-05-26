#  make helper function like mailing here.
from django.db import models
import uuid

class BaseModel(models.Model):
    uid = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    # treat me as class not model
    class Meta:
        abstract = True