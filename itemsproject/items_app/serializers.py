from rest_framework import serializers
from items_app.models import ItemsModel
 
class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemsModel
        fields = ['name','price']