from rest_framework import serializers
from .models import Dht
class ser(serializers.ModelSerializer):
    class Meta:
        model = Dht
        fields =['id','temp','dt']