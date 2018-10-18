from items.models import Item,FavoriteItem
from rest_framework import serializers
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [  
        'first_name',
        'last_name',
            ]       

class ItemListSerializer(serializers.ModelSerializer):
    added_by = UserSerializer()
    favorites= serializers.SerializerMethodField()
    detail = serializers.HyperlinkedIdentityField(
        view_name = "api-detail",
        lookup_field = "id",
        lookup_url_kwarg = "item_id"
        )
    class Meta:
        model = Item
        fields=['name','description','added_by','detail','added_by','favorites']  
    def get_favorites(self, obj):
        return obj.favoriteitem_set.count()
        
class ItemDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['__all__']            

