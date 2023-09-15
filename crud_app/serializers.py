from rest_framework import serializers
from .models import Person

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = '__all__'
 
class PersonByNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = '__all__'
        extra_kwargs = {
            'name': {'type': 'string'},
        }