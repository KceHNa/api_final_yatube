from django.urls import include, path
from rest_framework.routers import SimpleRouter

from api.views import (PostViewSet, GroupViewSet, CommentViewSet,
                       FollowViewSet)

app_name = 'api'


ver1 = SimpleRouter('v1')
ver1.register(r'posts', PostViewSet)
ver1.register(r'groups', GroupViewSet)
ver1.register(
    r'posts/(?P<post_id>[0-9]+)/comments',
    CommentViewSet,
    basename='comments'
)
ver1.register(r'follow', FollowViewSet, basename='follow')

urlpatterns = [
    path('v1/', include(ver1.urls)),
    path('v1/', include('djoser.urls.jwt')),
]
