from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from django.db.models import Q
from .serializers import *

class BaseModelViewSet(viewsets.ModelViewSet):
    model_mapping = {
        'aircraft': Aircraft,
        'airfield': Airfield,
        'flight': Flight,
        'imagepic': ImagePic,
        'limitrules': LimitRules,
        'myquery': MyQuery,
        'myquerybuild': MyQueryBuild,
        'pilot': Pilot,
        'qualification': Qualification,
        'settingconfig': SettingConfig
    }
    serializer_mapping = {
        'aircraft': AircraftSerializer,
        'airfield': AirfieldSerializer,
        'flight': FlightSerializer,
        'imagepic': ImagePicSerializer,
        'limitrules': LimitRulesSerializer,
        'myquery': MyQuerySerializer,
        'myquerybuild': MyQueryBuildSerializer,
        'pilot': PilotSerializer,
        'qualification': QualificationSerializer,
        'settingconfig': SettingConfigSerializer
    }


    def get_serializer_class(self):
        table_name = self.kwargs.get('table_name', '').lower()
        serializer_class = self.serializer_mapping.get(table_name)
        if serializer_class is None:
            raise ValueError(f"No serializer found for table_name: {table_name}")
        return serializer_class

    def get_queryset(self):
        table_name = self.kwargs.get('table_name', '').lower()
        model = self.model_mapping.get(table_name)
        if model:
            return model.objects.all()
        return None

    @action(detail=False, methods=['post'])
    def bulk_create(self, request, *args, **kwargs):
        table_name = request.data.get('table_name', '').lower()
        model = self.model_mapping.get(table_name)

        if model:
            serializer_class = self.get_serializer_class()
            serializer = serializer_class(data=request.data['items'], many=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({"detail": "Invalid table name"}, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['get'])
    def search(self, request, *args, **kwargs):
        search_query = request.query_params.get('search', '')
        table_name = request.query_params.get('table_name', '').lower()
        model = self.model_mapping.get(table_name)

        if model:
            queryset = model.objects.filter(Q(meta__icontains=search_query))
            serializer_class = self.get_serializer_class()
            serializer = serializer_class(queryset, many=True)
            return Response(serializer.data)
        return Response({"detail": "Invalid table name"}, status=status.HTTP_400_BAD_REQUEST)
