from django.db import models
class PilotData(models.Model):
    user_id = models.IntegerField()
    table = models.CharField(max_length=255)
    guid = models.UUIDField()
    platform = models.IntegerField()
    _modified = models.IntegerField()

    # Meta fields
    meta = models.JSONField()
