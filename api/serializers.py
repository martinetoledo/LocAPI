from rest_framework import serializers
from .models import Ubicacion


class UbicacionSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Ubicacion
        fields = ('fecha', 'lat', 'lng')
        read_only_fields = ['fecha']