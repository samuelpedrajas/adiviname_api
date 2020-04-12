from rest_framework import serializers
from .models import Game, GameClick, GameIcon, GameIconBase, Expression
from django.contrib.auth.models import User


class GameClickSerializer(serializers.ModelSerializer):  # create class to serializer model

    class Meta:
        model = GameClick
        fields = ('num_clicks',)


class GameIconSerializer(serializers.ModelSerializer):  # create class to serializer model
	url = serializers.SerializerMethodField()


	class Meta:
		model = GameIcon
		fields = ('url',)

	def get_url(self, game_icon):
		request = self.context.get('request')
		url = game_icon.file.url
		return request.build_absolute_uri(url)


class GameIconBaseSerializer(serializers.ModelSerializer):  # create class to serializer model
	url = serializers.SerializerMethodField()
	name = serializers.SerializerMethodField()

	class Meta:
		model = GameIconBase
		fields = ('url', 'name',)

	def get_url(self, game_icon_base):
		request = self.context.get('request')
		url = game_icon_base.file.url
		return request.build_absolute_uri(url)

	def get_name(self, game_icon_base):
		url = game_icon_base.file.url
		name = url[url.rfind("/") + 1:].split(".")[0]
		return name


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
	icon = GameIconSerializer()
	icon_base = GameIconBaseSerializer()

	def to_representation(self, instance):
		data = super(GameSerializer, self).to_representation(instance)
		since_datetime = self.context.get("since_datetime", False)
		if instance.updated_at < since_datetime:
			data.pop('title')
			data.pop('game_type')
			data.pop('updated_at')
			data.pop('created_at')
			data.pop('creator')
			data.pop('featured')
			data.pop('description')

		if instance.expressions_updated_at < since_datetime:
			data.pop('expressions')

		if instance.image_updated_at < since_datetime:
			data.pop('icon')

		if instance.image_base_updated_at < since_datetime:
			data.pop('icon_base')

		if data["clicks"] is None:
			data["clicks"] = 0

		return data

	class Meta:
		model = Game
		fields = ('id', 'title', 'icon', 'icon_base', 'featured', 'game_type', 'description', 'updated_at', 'created_at', 'creator', 'expressions', 'clicks')


class ExpressionSerializer(serializers.ModelSerializer):  # create class to serializer model

    class Meta:
        model = Expression
        fields = ('text',)


class UserSerializer(serializers.ModelSerializer):  # create class to serializer usermodel

    class Meta:
        model = User
        fields = ('id', 'username')
