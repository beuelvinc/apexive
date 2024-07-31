from rest_framework import serializers
from .models import Aircraft, Airfield, Flight, ImagePic, LimitRules, MyQuery, MyQueryBuild, Pilot, Qualification, \
    SettingConfig


class BaseModelSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        abstract = True


class AircraftSerializer(BaseModelSerializer):
    class Meta(BaseModelSerializer.Meta):
        model = Aircraft


class AirfieldSerializer(BaseModelSerializer):
    class Meta(BaseModelSerializer.Meta):
        model = Airfield


class FlightSerializer(BaseModelSerializer):
    class Meta(BaseModelSerializer.Meta):
        model = Flight


class ImagePicSerializer(BaseModelSerializer):
    class Meta(BaseModelSerializer.Meta):
        model = ImagePic


class LimitRulesSerializer(BaseModelSerializer):
    class Meta(BaseModelSerializer.Meta):
        model = LimitRules


class MyQuerySerializer(BaseModelSerializer):
    class Meta(BaseModelSerializer.Meta):
        model = MyQuery


class MyQueryBuildSerializer(BaseModelSerializer):
    class Meta(BaseModelSerializer.Meta):
        model = MyQueryBuild


class PilotSerializer(BaseModelSerializer):
    class Meta(BaseModelSerializer.Meta):
        model = Pilot


class QualificationSerializer(BaseModelSerializer):
    class Meta(BaseModelSerializer.Meta):
        model = Qualification


class SettingConfigSerializer(BaseModelSerializer):
    class Meta(BaseModelSerializer.Meta):
        model = SettingConfig
