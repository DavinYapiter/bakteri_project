from rest_framework import serializers
from .models import Bakteri, KategoriBakteri

class KategoriSerializer(serializers.ModelSerializer):
    class Meta:
        model = KategoriBakteri
        fields = '__all__'

class BakteriSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bakteri
        fields = '__all__'
