from rest_framework.serializers import ModelSerializer
from base.models import Room


# Serializes room objects into JSON data
class RoomSerializer(ModelSerializer):
    class Meta:
        model = Room
        fields = "__all__"