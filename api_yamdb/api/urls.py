from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (CategoryListCreateViewSet, CommentViewSet, GenreViewSet,
                    ReviewViewSet, TitleViewSet, UserViewSet, get_auth_token,
                    signup_user)

router_ver1 = DefaultRouter()

router_ver1.register(r'titles', TitleViewSet)
router_ver1.register(r'categories', CategoryListCreateViewSet,)
router_ver1.register(r'genres', GenreViewSet)
router_ver1.register(
    r'titles/(?P<title_id>[\d]+)/reviews',
    ReviewViewSet,
    basename='reviews',)
router_ver1.register(
    r'titles/(?P<title_id>[\d]+)/reviews/(?P<review_id>[\d]+)/comments',
    CommentViewSet,
    basename='comments',)
router_ver1.register(r'users', UserViewSet)

urlpatterns = [
    path('v1/auth/signup/', signup_user, name='signup'),
    path('v1/auth/token/', get_auth_token, name='auth'),
    path('v1/', include(router_ver1.urls)),
]
