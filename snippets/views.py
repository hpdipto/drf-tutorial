from django.contrib.auth.models import User
from rest_framework import mixins
from rest_framework import generics
from rest_framework import permissions

from .models import Snippet
from .serializers import SnippetSerializer, UserSerializer


class SnippetList(generics.ListCreateAPIView):
	"""
	List all snippents, or create a new snippet
	"""
	queryset = Snippet.objects.all()
	serializer_class = SnippetSerializer
	permission_classes = [permissions.IsAuthenticatedOrReadOnly]

	def perform_create(self, serializer):
		serializer.save(owner=self.request.user)


class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
	"""
	Retrieve, update or delete a snippet instance
	"""
	queryset = Snippet.objects.all()
	serializer_class = UserSerializer
	permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class UserList(generics.ListAPIView):
	queryset = User.objects.all()
	serializer_class = UserSerializer
		

class UserDetail(generics.RetrieveAPIView):
	queryset = User.objects.all()
	serializer_class = UserSerializer