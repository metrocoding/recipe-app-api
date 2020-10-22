from core.models import Tag, Ingrediant
from rest_framework import serializers


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('id', 'name')
        read_only_fields = ('id',)


class IngrediantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingrediant
        fields = ('id', 'name')
        read_only_fields = ('id',)
