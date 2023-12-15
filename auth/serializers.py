from django.contrib.auth import authenticate, get_user_model
from rest_framework import serializers

from models import User, Team


class TeamBaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ('id', 'name')

class UserBaseSerializer(serializers.ModelSerializer):
    team = TeamBaseSerializer(many=False)

    class Meta:
        model = User
        fields = ('id', 'username', 'team')


class UserRegisterSerializer(serializers.ModelSerializer):
    team = TeamBaseSerializer(many=False)

    class Meta:
        model = get_user_model()
        fields = ("username", "password", "team")

    def create(self, validated_data:dict):
        username = validated_data.get('username', None)
        userteam =  Team.objects.get(team_name=validated_data["team"])
        password = validated_data.get("password", None)
        
        user = User(username=username)
        user.set_password(password)
        user.team = userteam
        user.save()
        
        return user

class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True, write_only=True)

    def validate(self, data):
        username = data.get("username")
        password = data.get("password")

        user = authenticate(username=username, password=password)

        if user is None:
            raise serializers.DjangoValidationError("유저 정보 다시 한번 확인 해주세요")

        return user