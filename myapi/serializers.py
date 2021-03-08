from rest_framework import serializers
from .models import Record


class RecordSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Record
        lookup_field = 'id'
        fields = (
            'id',
            'timestamp',
            'value1',
            'value2',
            'value3'
        )
