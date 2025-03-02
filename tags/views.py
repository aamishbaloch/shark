from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import Tag
from .serializers import TagSerializer, TagDetailSerializer


class TagViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows tags to be viewed or edited.
    """
    queryset = Tag.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    def get_serializer_class(self):
        if self.action in ['retrieve', 'update', 'partial_update']:
            return TagDetailSerializer
        return TagSerializer

    def perform_create(self, serializer):
        tag = serializer.save()
        tag.users.add(self.request.user)
