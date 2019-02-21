from rest_framework import generics
from .serializers import UbicacionSerializer
from .models import Ubicacion


class CreateView(generics.ListCreateAPIView):
    queryset = Ubicacion.objects.all()
    serializer_class = UbicacionSerializer

    def perform_create(self, serializer):
        serializer.save()


class DetailsView(generics.RetrieveUpdateDestroyAPIView):
    """This class handles the http GET, PUT and DELETE requests."""

    queryset = Ubicacion.objects.all()
    serializer_class = UbicacionSerializer
