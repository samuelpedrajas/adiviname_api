from rest_framework import serializers
from .models import Game, Expression
from django.contrib.auth.models import User


class GameSerializer(serializers.ModelSerializer):  # create class to serializer model
    creator = serializers.ReadOnlyField(source='creator.username')

    class Meta:
        model = Game
        fields = ('id', 'title', 'description', 'creator')


class ExpressionSerializer(serializers.ModelSerializer):  # create class to serializer model

    class Meta:
        model = Expression
        fields = ('text',)


class UserSerializer(serializers.ModelSerializer):  # create class to serializer usermodel

    class Meta:
        model = User
        fields = ('id', 'username')
