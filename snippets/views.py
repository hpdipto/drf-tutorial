from rest_framework import mixins
from rest_framework import generics

from .models import Snippet
from .serializers import SnippetSerializer


class SnippetList(generics.ListCreateAPIView):
	"""
	List all snippents, or create a new snippet
	"""
	queryset = Snippet.objects.all()
	serializer_class = SnippetSerializer


class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
	"""
	Retrieve, update or delete a snippet instance
	"""
	queryset = Snippet.objects.all()
	serializer_class = SnippetSerializer
		