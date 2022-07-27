# system import
from rest_framework import serializers
# models import
from django.contrib.auth import get_user_model

User = get_user_model()

class ManagerListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('pk', 'username', 'name', 'belong', 'phone', 'rfid_num', 'campus', 'position')


class ManagerSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('pk', 'username', 'password', 'name', 'belong', 'phone', 'rfid_num', 'campus', 'position')


# 회원 정보 수정
class ManagerUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username', 'password', 'name', 'phone',)


class ManagerAllUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('name', 'belong', 'phone', 'rfid_num', 'position', 'username', 'password', 'is_superuser', )  # password..?