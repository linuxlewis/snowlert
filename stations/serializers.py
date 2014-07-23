from rest_framework import serializers, pagination
from rest_framework_gis.serializers import GeoModelSerializer
from stations.models import Station

class StationSerializer(GeoModelSerializer):
    data = serializers.SerializerMethodField('get_data')

    class Meta:
        model = Station
        fields = ('id', 'data','location','station_source')

    def get_data(self, obj):
        return obj.data
