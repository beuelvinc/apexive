from django.db import models


class BaseModel(models.Model):
    user_id = models.IntegerField()
    guid = models.UUIDField()
    platform = models.IntegerField()
    _modified = models.IntegerField()

    # Meta fields
    meta = models.JSONField()

    class Meta:
        abstract = True


class Aircraft(BaseModel):
    pass


class Airfield(BaseModel):
    pass


class Flight(BaseModel):
    pass


class ImagePic(BaseModel):
    pass


class LimitRules(BaseModel):
    pass


class MyQuery(BaseModel):
    pass


class MyQueryBuild(BaseModel):
    pass


class Pilot(BaseModel):
    pass


class Qualification(BaseModel):
    pass


class SettingConfig(BaseModel):
    pass
