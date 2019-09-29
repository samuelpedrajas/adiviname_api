from rest_framework import status
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Game, GameClick
from .serializers import GameSerializer
from .pagination import CustomPagination


class game_list(ListAPIView):
    serializer_class = GameSerializer
    # permission_classes = (IsAuthenticated,)
    pagination_class = CustomPagination
    
    def get_queryset(self):
       games = Game.objects.all()
       return games

    # Get all games
    def get(self, request):
        games = self.get_queryset()
        paginate_queryset = self.paginate_queryset(games)
        serializer = self.serializer_class(paginate_queryset, many=True)
        return self.get_paginated_response(serializer.data)


class game_click(APIView):

    throttle_scope = 'anonymous'

    def post(self, request, pk):
        try:
            game = Game.objects.get(id=pk)
            game_click, created = GameClick.objects.get_or_create(game_id=game)
            game_click.num_clicks += 1
            game_click.save()
            return Response(status=status.HTTP_200_OK)
        except Game.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
