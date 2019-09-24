from django.urls import path, re_path
from . import views


urlpatterns = [
    re_path(
    	r'^api/v1/game/(?P<pk>[0-9]+)$',
        views.expression_list.as_view(),
        name='expression_list'
    ),
    path(
    	'api/v1/game/',
        views.game_list.as_view(),
        name='game_list'
    )
]
