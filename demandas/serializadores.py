# /home/bruno/demando/demandas/serializadores.py

from rest_framework import serializers
from .models import Demanda

class DemandaSerializador(serializers.ModelSerializer):
    class Meta:
        model = Demanda
        fields = '__all__'
