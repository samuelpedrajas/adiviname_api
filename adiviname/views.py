from rest_framework.generics import ListAPIView
from .models import Game, Expression
from .serializers import ExpressionSerializer, GameSerializer
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


class expression_list(ListAPIView):
    serializer_class = ExpressionSerializer
    # permission_classes = (IsAuthenticated,)
    pagination_class = CustomPagination
    
    def get_queryset(self):
       expressions = Expression.objects.get()
       return expressions

    # Get all expressions
    def get(self, request):
        expressions = self.get_queryset()
        paginate_queryset = self.paginate_queryset(expressions)
        serializer = self.serializer_class(paginate_queryset, many=True)
        return self.get_paginated_response(serializer.data)
