from rest_framework import serializers
from .models import Adrule


class AdruleSerializer(serializers.ModelSerializer):
  class Meta:
    model = Adrule
    fields = ('id', 'title', 'author', 'description', 'rule', 'created_at')