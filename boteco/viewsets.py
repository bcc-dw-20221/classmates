from django.contrib.auth import get_user_model
from rest_framework import viewsets
from boteco.models import Perfil, Bebida, TipoDeCorno

from boteco.serializers import (
    PerfilSerializer,
    UserSerializer,
    BebidaSerializer,
    TipoDeCornoSerializer,
)


class UserViewSet(viewsets.ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer


class PerfilViewSet(viewsets.ModelViewSet):
    queryset = Perfil.objects.all()
    serializer_class = PerfilSerializer


class BebidaViewSet(viewsets.ModelViewSet):
    queryset = Bebida.objects.all()
    serializer_class = BebidaSerializer


class TipoDeCornoViewSet(viewsets.ModelViewSet):
    queryset = TipoDeCorno.objects.all()
    serializer_class = TipoDeCornoSerializer
