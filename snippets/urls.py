from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import SnippetViewSet, UserViewSet, api_root 
from . import views 
from rest_framework import renderers
from rest_framework.routers import DefaultRouter


# snippet_list = SnippetVieSet.as_view({
# 	'get': 'list',
# 	'post': 'create'
# })

# snippet_detail = SnippetViewSet.as_view({
# 	'get': 'retrieve',
# 	'put': 'update',
# 	'patch': 'partial_update',
# 	'delete': 'destroy'
# })

# snippet_highlight = SnippetViewSet.as_view({
# 	'get': 'highlight'
# })

# user_list = UserViewSet.as_view({
# 	'get': 'list'
# })

# user_detail = UserViewSet.as_view({
# 	'get': 'retrieve'
# })

# urlpatterns = [
# 	path('', api_root),
# 	path('snippets/', snippet_list, name='snippet-list'),
# 	path('snippets/<int:pk>/', snippet_detail, name='snippet-detail'),
# 	path('snippets/<int:pk>/highlight/', snippet_highlight, 'snippet-highlight'),
# 	path('users/', user_list, name='user-list'),
# 	path('users/<int:pk>/', user_detail, name='user-detail'),
# ]

# urlpatterns = format_suffix_patterns(urlpatterns)


# Create a router and register our viewsets with it
router = DefaultRouter()
router.register(r'snippets', views.SnippetViewSet)
router.register(r'users', views.UserViewSet)

# The API URLs are now determined automatically by the router
urlpatterns = [
	path(r'', include(router.urls)),
]