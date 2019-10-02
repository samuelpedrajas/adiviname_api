from rest_framework import serializers
from .models import Game, GameClick, Expression
from django.contrib.auth.models import User


class GameClickSerializer(serializers.ModelSerializer):  # create class to serializer model

    class Meta:
        model = GameClick
        fields = ('num_clicks',)

class GameSerializer(serializers.ModelSerializer):  # create class to serializer model
	creator = serializers.ReadOnlyField(source='creator.username')
	expressions = serializers.SlugRelatedField(
		many=True,
		read_only=True,
		slug_field='text'
	)
	clicks = serializers.SlugRelatedField(
		many=False,
		read_only=True,
		slug_field='num_clicks'
	)
	def to_representation(self, instance):
		data = super(GameSerializer, self).to_representation(instance)
		since_datetime = self.context.get("since_datetime", False)
		if instance.updated_at < since_datetime:
			data.pop('title')
			data.pop('description')
			data.pop('game_type')
			data.pop('updated_at')
			data.pop('created_at')
			data.pop('creator')
			data.pop('expressions')

		if data["clicks"] is None:
			data["clicks"] = 0

		return data

	class Meta:
		model = Game
		fields = ('id', 'title', 'description', 'game_type', 'updated_at', 'created_at', 'creator', 'expressions', 'clicks')


class ExpressionSerializer(serializers.ModelSerializer):  # create class to serializer model

    class Meta:
        model = Expression
        fields = ('text',)


class UserSerializer(serializers.ModelSerializer):  # create class to serializer usermodel

    class Meta:
        model = User
        fields = ('id', 'username')
