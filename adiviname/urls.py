from django.urls import path, re_path
from . import views


urlpatterns = [
    re_path(
    	r'^api/v1/game_click/(?P<pk>[0-9]+)$',
        views.game_click.as_view(),
        name='game_click'
    ),
    path(
    	'api/v1/game/',
        views.game_list.as_view(),
        name='game_list'
    )
]
