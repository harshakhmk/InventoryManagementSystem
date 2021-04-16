from rest_framework import serializers
from .models import *  
class EquipmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Equipment
        fields=['id','name','issued','send_to_manager']

class AccessRequestSerializer(serializers.ModelSerializer):
    user_type = serializers.ChoiceField(choices=' Request_States')
    class Meta:
        model = AccessRequest
        fields=['id','access_request','issued_element','user_type']
        