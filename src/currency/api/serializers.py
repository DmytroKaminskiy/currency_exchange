from rest_framework import serializers
from currency.models import Rate


class RateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Rate
        fields = ('id', 'created', 'currency', 'buy', 'sale', 'source')
