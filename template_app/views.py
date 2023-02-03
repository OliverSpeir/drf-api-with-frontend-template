from rest_framework import generics
from .serializers import ItemSerializer
from .models import Item
from .permissions import IsCreatorOrReadOnly


class ItemList(generics.ListCreateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer


class ItemDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsCreatorOrReadOnly,)
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
