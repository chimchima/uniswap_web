from rest_framework import serializers
from . import models

class SwapSerializers(serializers.ModelSerializer):

    class Meta:
        model = models.Swap
        fields = ('token_in', 'token_out', 'amount_in', 'amount_out')