from rest_framework import serializers
from .models import Game, Expression
from django.contrib.auth.models import User


class GameSerializer(serializers.ModelSerializer):  # create class to serializer model
	creator = serializers.ReadOnlyField(source='creator.username')
	expressions = serializers.SlugRelatedField(
		many=True,
		read_only=True,
		slug_field='text'
	)

	def to_representation(self, instance):
		data = super(GameSerializer, self).to_representation(instance)
		since_datetime = self.context.get("since_datetime", False)
		if instance.updated_at < since_datetime:
			data.pop('expressions')

		return data

	class Meta:
		model = Game
		fields = ('id', 'title', 'description', 'updated_at', 'created_at', 'creator', 'expressions', 'clicks')


class ExpressionSerializer(serializers.ModelSerializer):  # create class to serializer model

    class Meta:
        model = Expression
        fields = ('text',)


class UserSerializer(serializers.ModelSerializer):  # create class to serializer usermodel

    class Meta:
        model = User
        fields = ('id', 'username')
