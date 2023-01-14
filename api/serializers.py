from rest_framework import serializers


class UserSerializer(serializers.Serializer):
    id = serializers.CharField(read_only=True)
    name = serializers.CharField()
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()


class ProviderSerializer(serializers.Serializer):
    id = serializers.CharField()
    name = serializers.CharField()
    logo = serializers.URLField()
    about = serializers.CharField()


class PlanSerializer(serializers.Serializer):
    id = serializers.CharField()
    name = serializers.CharField()
    about = serializers.CharField()
    category = serializers.CharField()
    keys = serializers.JSONField()
    provider = ProviderSerializer()
