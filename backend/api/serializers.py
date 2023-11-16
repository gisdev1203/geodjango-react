from rest_framework import serializers
from .models import PlRiver3857

class PlRiver3857Serializer(serializers.ModelSerializer):
    
    class Meta:
        model = PlRiver3857
        fields = "__all__"
        # fields = ('pk', 'name', 'email', 'document', 'phone', 'registrationDate','photo')