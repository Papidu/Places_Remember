from rest_framework.serializers import ModelSerializer

from remembers.models import RememberCards


class RememberCardsSerializer(ModelSerializer):
    class Meta:
        model = RememberCards
        fields = '__all__'
