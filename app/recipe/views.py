from rest_framework import viewsets, mixins
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from core.models import Tag, Ingrediant
from recipe import serializers


class BaseRecipeAttrViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        # get only entity for current authenticated user
        return self.queryset.filter(user=self.request.user).order_by('-name')

    def perform_create(self, serializer):
        # create entity by authenticated user
        serializer.save(user=self.request.user)


class TagViewSet(BaseRecipeAttrViewSet):
    queryset = Tag.objects.all()
    serializer_class = serializers.TagSerializer


class IngrediantViewSet(BaseRecipeAttrViewSet):
    queryset = Ingrediant.objects.all()
    serializer_class = serializers.IngrediantSerializer
