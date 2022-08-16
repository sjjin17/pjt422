from rest_framework import serializers
from ..models import Building, Floor, Student, Trashbin, Group
from django.contrib.auth import get_user_model

# 해당 층에 쓰레기통 추가
class TrashbinCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Trashbin
        exclude = ('group', 'discard_users', )


# 쓰레기통 상세 조회
class TrashbinSerializer(serializers.ModelSerializer):
    # discard_users를 조회하기 위한 관리자 정보
    class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = get_user_model()
            excludes = ('created_at', 'updated_at',)

    discard_users = UserSerializer(many=True, read_only=True)
    
    class Meta:
        model = Trashbin
        fields = '__all__'


class TrashbinNotificationSerializer(serializers.ModelSerializer):
    
    class GroupSerializer(serializers.ModelSerializer):

        class FloorSerializer(serializers.ModelSerializer):
            
            class BuildingSerializer(serializers.ModelSerializer):

                class Meta:
                    model = Building
                    fields = ('pk', 'name',)
                
            building = BuildingSerializer(read_only=True)

            class Meta:
                model = Floor
                fields = ('pk', 'name', 'building')
        
        floor = FloorSerializer(read_only=True)

        class Meta:
            model = Group
            fields = ('pk', 'name', 'floor')
    
    group = GroupSerializer(read_only=True)

    class Meta:
        model = Trashbin
        fields = '__all__'
