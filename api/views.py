from rest_framework import viewsets
from pokedex.models import Pokemon
from .serializers import PokemonSerializers

class PokemonViewSet(viewsets.ModelViewSet):
    queryset = Pokemon.objects.all()
    serializer_class = PokemonSerializers