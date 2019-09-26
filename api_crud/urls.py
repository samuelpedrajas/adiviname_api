
from django.contrib import admin
from django.conf.urls import include, url, re_path
from django.conf import settings
from django.views.static import serve

from .views import RegisterView, CustomLoginView


# urls
urlpatterns = [
    url(r'^', include('adiviname.urls')),
    url(r'^rest-auth/login/', CustomLoginView.as_view()),
    url(r'^rest-auth/registration/', RegisterView.as_view()),
    url(r'^rest-auth/', include('rest_auth.urls')),
    url(r'^admin/', admin.site.urls),
    re_path(r'^static/(?P<path>.*)$', serve,
            {'document_root': settings.STATIC_ROOT}),
]