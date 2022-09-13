from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from rest_framework import serializers
from rest_framework.response import Response

from boteco.models import Perfil, Bebida, TipoDeCorno


class BebidaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Bebida
        fields = "__all__"


class TipoDeCornoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TipoDeCorno
        fields = "__all__"


class CreateUserSerializer(serializers.HyperlinkedModelSerializer):
    password = serializers.CharField(
        write_only=True,
        required=True,
        style={"input_type": "password", "placeholder": "password"},
    )

    class Meta:
        model = get_user_model()
        fields = [
            "url",
            "username",
            "password",
            "email",
            "first_name",
            "last_name",
        ]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        validated_data["password"] = make_password(
            validated_data.get("password")
        )
        return super(CreateUserSerializer, self).create(validated_data)


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ["url", "username", "first_name", "last_name"]


class PerfilSerializer(serializers.HyperlinkedModelSerializer):
    user = CreateUserSerializer(required=True)

    class Meta:
        model = Perfil
        fields = [
            "url",
            "user",
            "foto_perfil",
            "qtd_chifres",
            "status",
            "ultimo_chifre",
            "bebida_preferida",
            "procurando_mais",
        ]

    def create(self, validated_data):
        """
        Overriding the default create method of the Model serializer.
        :param validated_data: data containing all the details of perfil
        :return: returns a successfully created perfil record
        """
        user_data = validated_data.pop("user")
        user = CreateUserSerializer.create(
            CreateUserSerializer(), validated_data=user_data
        )
        if user.pk:
            perfil, created = Perfil.objects.update_or_create(
                user=user,
                foto_perfil=validated_data.pop("foto_perfil"),
                qtd_chifres=validated_data.pop("qtd_chifres"),
                status=validated_data.pop("status"),
                ultimo_chifre=validated_data.pop("ultimo_chifre"),
                bebida_preferida=validated_data.pop("bebida_preferida"),
                procurando_mais=validated_data.pop("procurando_mais"),
            )
            if created:
                return perfil
        else:
            user.delete()
        return Response(
            {"message": "Não pude criar um novo perfil."}, status=406
        )
