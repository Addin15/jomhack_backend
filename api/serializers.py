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
    phone = serializers.CharField(max_length=15)
    email = serializers.EmailField()
    website = serializers.URLField()


class PlanSerializer(serializers.Serializer):
    id = serializers.CharField()
    name = serializers.CharField()
    about = serializers.CharField()
    category = serializers.CharField()
    keys = serializers.JSONField()
    provider = ProviderSerializer()

class NewsSerializer(serializers.Serializer):
    id = serializers.CharField()
    title = serializers.CharField(max_length=100)
    about = serializers.CharField()
    category = serializers.CharField(max_length=100)
    keys = serializers.JSONField()
    link = serializers.URLField()
