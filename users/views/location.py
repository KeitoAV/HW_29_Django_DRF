from rest_framework.viewsets import ModelViewSet

from users.models.location import Location
from users.serializers.location import LocationSerializer


class LocationViewSet(ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
