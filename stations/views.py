from django.shortcuts import render

from rest_framework import viewsets, filters
from rest_framework_gis.filters import InBBOXFilter

from stations.models import Station
from stations.serializers import StationSerializer

# Create your views here.
class StationViewSet(viewsets.ReadOnlyModelViewSet): 

    queryset = Station.objects.all()
    serializer_class = StationSerializer
    bbox_filter_field = 'location'
    filter_backends = (InBBOXFilter, filters.DjangoFilterBackend)

def map_view(request):
    return render(request, 'stations/map.html')
