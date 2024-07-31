from django.db import models
class Aircraft(models.Model):
    user_id = models.IntegerField()
    guid = models.UUIDField()
    platform = models.IntegerField()
    _modified = models.IntegerField()

    # Meta fields
    meta = models.JSONField()



class Flight(models.Model):
    user_id = models.IntegerField()
    guid = models.UUIDField()
    platform = models.IntegerField()
    _modified = models.IntegerField()

    # Meta fields
    meta = models.JSONField()

