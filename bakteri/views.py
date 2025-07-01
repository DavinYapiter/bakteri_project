from rest_framework import viewsets
from .models import Bakteri, KategoriBakteri
from .serializers import BakteriSerializer, KategoriSerializer

class KategoriViewSet(viewsets.ModelViewSet):
    queryset = KategoriBakteri.objects.all()
    serializer_class = KategoriSerializer

class BakteriViewSet(viewsets.ModelViewSet):
    queryset = Bakteri.objects.all()
    serializer_class = BakteriSerializer
