from rest_framework import viewsets
from .serializers import PizzaSerializer
from .models import Pizza


class PizzaViewset(viewsets.ReadOnlyModelViewSet):
    queryset = Pizza.objects.all()
    serializer_class = PizzaSerializer
