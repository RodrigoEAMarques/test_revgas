from rest_framework import serializers
from .models import Banco

class BancoSeralizers(serializers.ModelSerializer):
    class Meta:
        model = Banco
        fields = '__all__'