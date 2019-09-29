from django.urls import path, re_path
from . import views


urlpatterns = [
    re_path(
    	r'^api/v1/game_click/(?P<pk>[0-9]+)$',
        views.GameClickView.as_view(),
        name='game_click'
    ),
    path(
    	'api/v1/game/',
        views.GameListView.as_view(),
        name='game_list'
    )
]
